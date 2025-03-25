import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import col, explode, from_json, lit, year, month, dayofmonth
from pyspark.sql.types import StructType, StructField, ArrayType, StringType, DoubleType, LongType

# 1) Captura dos parâmetros do Glue (JOB_NAME)
args = getResolvedOptions(sys.argv, ["JOB_NAME"])

# 2) Inicialização do Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# 3) Definição dos caminhos S3 (Trusted e Refined)
TRUSTED_PATH = "s3://vm-sprint05/Trusted"
REFINED_PATH = "s3://vm-sprint05/Refined"

# 4) Definição de schema para parsear o campo 'detalhes_credits'
credits_schema = StructType([
    StructField("cast", ArrayType(
        StructType([
            StructField("id", LongType(), True),
            StructField("name", StringType(), True),
            StructField("popularity", DoubleType(), True),
            StructField("character", StringType(), True),
            StructField("order", LongType(), True)
        ])
    ), True)
    # Se necessário, incluir 'crew'
])

# 5) Leitura dos dados da camada Trusted (usando curingas para particionamento)
print("\nLendo arquivos da camada Trusted...")

df_reviews = spark.read.parquet(f"{TRUSTED_PATH}/TMDB/Parquet/Reviews/*/*/*/")
df_detalhes = spark.read.parquet(f"{TRUSTED_PATH}/TMDB/Parquet/Detalhes/*/*/*/")
df_csv = spark.read.parquet(f"{TRUSTED_PATH}/Local/CSV/*/*/*/")

print(f"Reviews: {df_reviews.count()} registros")
print(f"Detalhes: {df_detalhes.count()} registros")
print(f"CSV: {df_csv.count()} registros")

# 6) Criação da Tabela Fato (fato_series) a partir de df_reviews
print("\nCriando tabela fato_series...")

fato_series = df_reviews.select(
    col('id').alias('id_tmdb'),
    col('vote_average').alias('nota_media'),
    col('vote_count').alias('votos_totais'),
    col('popularity').alias('popularidade'),
    col('first_air_date').alias('data_lancamento')
).distinct()

# Valores fictícios para temporada e episódio (caso não haja dados específicos)
fato_series = fato_series.withColumn("temporada", lit(1))
fato_series = fato_series.withColumn("episodio", lit(1))

# 7) Criação da Dimensão Série (dim_serie) integrando dados do JSON (TMDB) e CSV
print("\nCriando dimensão de séries (dim_serie) com chaves separadas...")

# Dados provenientes do JSON (TMDB)
dim_serie_json = df_detalhes.select(
    col('serie_id').alias('id_tmdb'),
    lit(None).cast("string").alias('id_csv'),
    col('serie_name').alias('nome'),
    col('serie_genre_ids').cast('string').alias('genero'),
    col('serie_original_language').alias('idioma_original'),
    col('serie_origin_country').cast('string').alias('pais_origem'),
    col('serie_first_air_date').alias('ano_lancamento'),
    col('detalhes_status').alias('status')
)

# Dados provenientes do CSV
dim_serie_csv = df_csv.select(
    lit(None).cast("bigint").alias('id_tmdb'),
    col('id').alias('id_csv'),
    col('titulopincipal').alias('nome'),
    col('genero').alias('genero'),
    lit(None).cast("string").alias('idioma_original'),
    lit(None).cast("string").alias('pais_origem'),
    col('anolancamento').alias('ano_lancamento'),
    lit(None).alias('status')
)

# União das duas fontes para formar a dimensão completa
dim_serie = dim_serie_json.unionByName(dim_serie_csv).distinct()

# 8) Parse do campo 'detalhes_credits' e criação da Dimensão Elenco (dim_elenco)
print("\nProcessando o campo detalhes_credits e criando dimensão de elenco...")

df_detalhes_parse = df_detalhes.withColumn(
    "credits_struct",
    from_json(col("detalhes_credits"), credits_schema)
)

df_cast = df_detalhes_parse.select(
    col('serie_id').alias('id_tmdb'),
    explode(col('credits_struct.cast')).alias('cast')
).where(col('cast').isNotNull())

dim_elenco = df_cast.select(
    col('cast.id').alias('elenco_id'),
    col('id_tmdb'),
    col('cast.name').alias('nome_ator'),
    col('cast.popularity').alias('popularidade_ator'),
    col('cast.character').alias('personagem'),
    col('cast.order').alias('ordem')
).distinct()

# 9) Criação da Dimensão Tempo (dim_tempo) a partir de fato_series
print("\nCriando dimensão de tempo...")

dim_tempo = fato_series.select(
    col('data_lancamento').alias('data_completa')
).distinct()

dim_tempo = dim_tempo.withColumn('ano', year(col('data_completa'))) \
                     .withColumn('mes', month(col('data_completa'))) \
                     .withColumn('dia', dayofmonth(col('data_completa')))

# 10) Criação da Dimensão Sentimento (dim_sentimento) a partir de df_reviews
print("\nCriando dimensão de sentimento (básica)...")

dim_sentimento = df_reviews.select(
    col('id').alias('id_tmdb'),
    col('overview').alias('texto_overview')
).distinct()

# 11) Salvando as tabelas no formato Parquet na camada Refined
print("\nSalvando tabelas na camada Refined...")

fato_series.write.mode("overwrite").parquet(f"{REFINED_PATH}/fato_series/")
dim_serie.write.mode("overwrite").parquet(f"{REFINED_PATH}/dim_serie/")
dim_elenco.write.mode("overwrite").parquet(f"{REFINED_PATH}/dim_elenco/")
dim_tempo.write.mode("overwrite").parquet(f"{REFINED_PATH}/dim_tempo/")
dim_sentimento.write.mode("overwrite").parquet(f"{REFINED_PATH}/dim_sentimento/")

print("\nJob finalizado com sucesso!")
job.commit()
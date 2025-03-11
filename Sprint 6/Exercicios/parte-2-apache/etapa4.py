from pyspark.sql import SparkSession
from pyspark.sql.functions import array, lit, floor, rand

# Inicializa a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Etapa4AdicionarPais") \
    .getOrCreate()

# Lê o arquivo, renomeia a coluna "_c0" para "Nomes" (se ainda não foi feito)
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Cria um array com os 13 países da América do Sul
paises = array(
    lit("Argentina"),
    lit("Bolivia"),
    lit("Brasil"),
    lit("Chile"),
    lit("Colombia"),
    lit("Equador"),
    lit("Guiana"),
    lit("Paraguai"),
    lit("Peru"),
    lit("Suriname"),
    lit("Uruguai"),
    lit("Venezuela"),
    lit("Guiana Francesa")
)

# Adiciona a coluna "País" escolhendo aleatoriamente um país do array.
# Usamos getItem com índice aleatório (0 a 12), obtido por floor(rand()*13)
df_nomes = df_nomes.withColumn("Pais", paises.getItem(floor(rand()*13).cast("int")))

# Exibe o schema e 10 linhas para verificação
df_nomes.printSchema()
df_nomes.show(10)

spark.stop()

import sys
import logging
import re
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.functions import input_file_name
from pyspark.sql.types import ArrayType, StringType

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Captura de parâmetros do Glue
# JOB_NAME = Nome do job no Glue
# TMDB_INPUT_PATH = Caminho para o diretório contendo os arquivos JSON
# TMDB_OUTPUT_PATH = Caminho de saída para os arquivos Parquet
args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'TMDB_INPUT_PATH',
    'TMDB_OUTPUT_PATH'
])

# Inicializa Spark e Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Inicializa o job no Glue
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Log dos parâmetros recebidos
logger.info("Iniciando Job de JSON (TMDB) com leitura recursiva.")
logger.info(f"TMDB_INPUT_PATH = {args['TMDB_INPUT_PATH']}")
logger.info(f"TMDB_OUTPUT_PATH = {args['TMDB_OUTPUT_PATH']}")

# Atribui os caminhos para facilitar o uso
tmdb_input = args['TMDB_INPUT_PATH']
tmdb_output = args['TMDB_OUTPUT_PATH']

try:
    # Leitura dos arquivos JSON (com busca em subdiretórios)
    logger.info("Lendo JSON de TMDB de forma recursiva...")
    df_tmdb = spark.read \
        .option("recursiveFileLookup", "true") \
        .option("multiLine", True) \
        .json(tmdb_input)
    logger.info(f"DataFrame lido possui {df_tmdb.count()} registros.")

    # Extrai o caminho do arquivo para identificar ano, mês e dia
    logger.info("Extraindo o caminho dos arquivos para identificar ano, mês e dia...")
    df_tmdb = df_tmdb.withColumn("input_file", input_file_name())

    # Função para extrair data do caminho do arquivo (formato: /ano/mes/dia/)
    def extract_date(path):
        match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', path)
        if match:
            return list(match.groups())
        else:
            return ["9999", "99", "99"]  # Valores padrão em caso de falha

    # Cria uma UDF para aplicar a função nos caminhos dos arquivos
    extract_date_udf = F.udf(extract_date, ArrayType(StringType()))

    # Aplica a UDF para criar uma coluna com os valores extraídos (ano, mês e dia)
    df_tmdb = df_tmdb.withColumn("date_tuple", extract_date_udf(F.col("input_file")))

    # Cria colunas separadas para ano, mês e dia
    df_tmdb = df_tmdb.withColumn("ano", F.col("date_tuple").getItem(0)) \
                     .withColumn("mes", F.col("date_tuple").getItem(1)) \
                     .withColumn("dia", F.col("date_tuple").getItem(2))

    # Grava os dados em formato Parquet, particionado por ano/mês/dia
    logger.info("Gravando os dados em Parquet particionado por ano/mes/dia...")
    df_tmdb.write \
        .mode("overwrite") \
        .partitionBy("ano", "mes", "dia") \
        .format("parquet") \
        .save(tmdb_output)
    logger.info("Dados JSON (TMDB) salvos com sucesso em Parquet.")

except Exception as e:
    # Captura erros e registra no log
    logger.error(f"Erro durante o processamento do TMDB: {e}")
    raise

# Finaliza o job após execução bem-sucedida
job.commit()
logger.info("Job de JSON (TMDB) finalizado com sucesso.")

import sys
import logging
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

# Configuração básica de logging
# Define o formato das mensagens de log e o nível de detalhamento
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Captura os parâmetros que serão passados via AWS Glue
# JOB_NAME = Nome do job no Glue
# MOVIES_INPUT_PATH = Caminho do CSV de filmes
# SERIES_INPUT_PATH = Caminho do CSV de séries
# TRUSTED_CSV_OUTPUT_PATH = Caminho de saída para o arquivo final em formato Parquet
args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'MOVIES_INPUT_PATH',
    'SERIES_INPUT_PATH',
    'TRUSTED_CSV_OUTPUT_PATH'
])

# Inicializa o SparkContext e o GlueContext (necessário para AWS Glue)
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Inicializa o job do Glue com os parâmetros capturados
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Log dos parâmetros capturados para conferência
logger.info("Iniciando Job de CSV. Parâmetros capturados:")
logger.info(f"MOVIES_INPUT_PATH = {args['MOVIES_INPUT_PATH']}")
logger.info(f"SERIES_INPUT_PATH = {args['SERIES_INPUT_PATH']}")
logger.info(f"TRUSTED_CSV_OUTPUT_PATH = {args['TRUSTED_CSV_OUTPUT_PATH']}")

# Atribui os caminhos dos arquivos CSV a variáveis para facilitar a manipulação
movies_path = args['MOVIES_INPUT_PATH']
series_path = args['SERIES_INPUT_PATH']
trusted_csv_path = args['TRUSTED_CSV_OUTPUT_PATH']

try:
    # Leitura do arquivo CSV de filmes
    # option("header", True) => Considera a primeira linha como cabeçalho
    logger.info("Lendo CSV de filmes...")
    df_movies = spark.read.option("header", True).csv(movies_path)
    logger.info(f"DataFrame de filmes possui {df_movies.count()} registros.")

    # Leitura do arquivo CSV de séries
    logger.info("Lendo CSV de séries...")
    df_series = spark.read.option("header", True).csv(series_path)
    logger.info(f"DataFrame de séries possui {df_series.count()} registros.")

    # União dos DataFrames (de filmes e séries)
    # allowMissingColumns=True => Permite que colunas faltantes em um dos DataFrames sejam preenchidas com valores nulos
    logger.info("Unindo DataFrames de filmes e séries...")
    df_all = df_movies.unionByName(df_series, allowMissingColumns=True)
    logger.info(f"DataFrame combinado possui {df_all.count()} registros.")

    # Exemplo de transformação de colunas (opcional)
    # Se precisar converter tipos de dados, usar o trecho abaixo:
    # logger.info("Convertendo tipos de colunas, se necessário...")
    # df_all = df_all.withColumn("col_exemplo", F.col("col_exemplo").cast("Integer"))

    # Escrita dos dados combinados no formato Parquet
    # mode("overwrite") => Substitui o arquivo existente, se já existir
    logger.info("Gravando DataFrame em formato Parquet (sem particionamento)...")
    df_all.write.mode("overwrite").format("parquet").save(trusted_csv_path)
    logger.info("Dados salvos com sucesso em Parquet na camada Trusted.")

# Tratamento de erro padrão
# Em caso de falha, o erro será registrado nos logs
except Exception as e:
    logger.error(f"Erro durante processamento CSV: {e}")
    raise

# Finaliza o job no Glue após execução bem-sucedida
job.commit()
logger.info("Job de CSV finalizado com sucesso.")
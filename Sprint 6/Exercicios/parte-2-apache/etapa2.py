from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

# Inicializando a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Etapa2RenomearColuna") \
    .getOrCreate()

# Lê o arquivo nomes_aleatorios.txt (sem cabeçalho, schema inferido)
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

# Renomeia a coluna '_c0' para 'Nomes'
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Imprime o schema (para ver o tipo de cada coluna)
df_nomes.printSchema()

# Mostra as 10 primeiras linhas
df_nomes.show(10)

# Finaliza a sessão Spark
spark.stop()

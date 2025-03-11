from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext

# Inicializando SparkSession com suporte a SQL
spark = SparkSession \
    .builder \
    .master('local[*]') \
    .appName('Exercicio Intro') \
    .getOrCreate()

# Carregando o arquivo nomes_aleatorios.txt como CSV (cada linha é uma entrada)
df_nomes = spark.read.csv('nomes_aleatorios.txt', header=False, inferSchema=True)

# Exibindo as 5 primeiras linhas do DataFrame
df_nomes.show(5)

# Finalizando a sessão Spark após o uso
spark.stop()

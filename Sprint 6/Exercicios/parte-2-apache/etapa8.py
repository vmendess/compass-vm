from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand, floor

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Etapa8Millennials") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adiciona seed para consistência
df_nomes = df_nomes.withColumn("AnoNascimento", floor(rand(seed=42)*75 + 1940))

millennials = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994))

print("Numero de pessoas Millennials no dataset:", millennials.count())

spark.stop()

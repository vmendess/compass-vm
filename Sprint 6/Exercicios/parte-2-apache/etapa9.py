from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, floor

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Etapa9SQLMillennials") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adiciona seed para consistência
df_nomes = df_nomes.withColumn("AnoNascimento", floor(rand(seed=42)*75 + 1940))

df_nomes.createOrReplaceTempView("pessoas")

resultado = spark.sql("""
SELECT COUNT(*) AS Quantidade_Millennials
FROM pessoas
WHERE AnoNascimento BETWEEN 1980 AND 1994
""")

resultado.show()

spark.stop()

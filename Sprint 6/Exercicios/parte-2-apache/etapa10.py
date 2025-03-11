from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Etapa10AgrupamentoGeracoes") \
    .getOrCreate()

# Carrega dataset e adiciona colunas
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Gera AnoNascimento e País aleatoriamente, se necessário
from pyspark.sql.functions import rand, floor, when
df_nomes = df_nomes.withColumn("AnoNascimento", floor(rand()*75 + 1940))
df_nomes = df_nomes.withColumn("Pais", when(rand() > 0.5, "Brasil").otherwise("EUA"))

# Cria a tabela temporária
df_nomes.createOrReplaceTempView("pessoas")

# Executa agrupamento por país e geração
df_geracoes = spark.sql("""
SELECT Pais, 
       CASE
          WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
          WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geracao X'
          WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
          WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z'
       END AS Geracao,
       COUNT(*) AS Quantidade
FROM pessoas
WHERE AnoNascimento BETWEEN 1944 AND 2015
GROUP BY Pais, Geracao
ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
""")

df_geracoes.show(truncate=False)

spark.stop()

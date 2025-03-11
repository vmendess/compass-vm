from pyspark.sql import SparkSession
from pyspark.sql.functions import floor, rand

# Inicializa a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Etapa5AnoNascimento") \
    .getOrCreate()

# Lê o arquivo e renomeia a coluna padrão para "Nomes"
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adiciona a coluna "AnoNascimento" com valores aleatórios entre 1945 e 2010
# Há 66 anos possíveis (de 1945 a 2010)
df_nomes = df_nomes.withColumn("AnoNascimento", floor(rand() * 66) + 1945)

# Exibe o schema e as 10 primeiras linhas para verificação
df_nomes.printSchema()
df_nomes.show(10)

spark.stop()

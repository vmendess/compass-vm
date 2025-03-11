from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inicializa a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Etapa6FiltrarNascidosEsteSeculo") \
    .getOrCreate()

# Lê o arquivo original e renomeia a coluna padrão para "Nomes"
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adiciona novamente a coluna "AnoNascimento" gerada na etapa anterior (necessário!)
from pyspark.sql.functions import rand
df_nomes = df_nomes.withColumn("AnoNascimento", (rand() * (2010 - 1945) + 1945).cast("integer"))

# Seleciona apenas a coluna "Nomes" e filtra para quem nasceu a partir de 2001
df_select = df_nomes.select("Nomes").where(col("AnoNascimento") >= 2001)

# Mostra 10 linhas desse novo DataFrame
df_select.show(10)

spark.stop()

from pyspark.sql import SparkSession
from pyspark.sql.functions import floor, rand

# Inicializa a SparkSession
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Etapa7SQL") \
    .getOrCreate()

# Lê o arquivo e renomeia a coluna padrão para "Nomes"
df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Adiciona a coluna "AnoNascimento" (como na etapa 5)
# Gera um valor aleatório entre 0 e 65, somado a 1945 para chegar ao intervalo 1945 a 2010
df_nomes = df_nomes.withColumn("AnoNascimento", floor(rand() * 66) + 1945)

# Registra o DataFrame como uma tabela temporária para o Spark SQL
df_nomes.createOrReplaceTempView("pessoas")

# Usa Spark SQL para selecionar as pessoas nascidas neste século (a partir de 2001)
df_select = spark.sql("SELECT Nomes FROM pessoas WHERE AnoNascimento >= 2001")

# Exibe 10 nomes do DataFrame resultante
df_select.show(10)

spark.stop()

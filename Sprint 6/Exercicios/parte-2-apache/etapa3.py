from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, when, col

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Etapa3AdicionarEscolaridade") \
    .getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes = df_nomes.withColumn("rand_val", rand())

df_nomes = df_nomes.withColumn(
    "Escolaridade",
    when(col("rand_val") < 0.33, "Fundamental")
     .when((col("rand_val") >= 0.33) & (col("rand_val") < 0.66), "Medio")
     .otherwise("Superior")
)

df_nomes = df_nomes.drop("rand_val")

df_nomes.printSchema()
df_nomes.show(10)

print("Fim da execucao da Etapa 3")

spark.stop()

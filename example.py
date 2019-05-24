from pyspark.sql import SparkSession

spark = SparkSession \
.builder \
.getOrCreate()

df = spark.createDataFrame([
    [1, 'Stefan'],
    [2, 'Raymond'],
    [3, 'Sanne'],
], ['id', 'name'])

df.show()

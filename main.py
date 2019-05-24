from pyspark.sql import SparkSession
spark = SparkSession\
.builder\
.getOrCreate()

print("Testing simple count")

# The Spark code will execute on the Azure Databricks cluster.
print(spark.range(100).count())

from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .appName('SparkPractice') \
        .master("local[*]") \
        .getOrCreate()

print(F"Spark session created successfully!")
print(F"Spark version: {spark.version}")
# Stop the Spark session
spark.stop()
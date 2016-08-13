__author__ = "Varatharajan Giri"

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("PythonSQL") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()


df = spark.createDataFrame(
    [(50, 100, ("General", .3493, "normal")), (100, 250, ("outofbox", .3435, "critical"))], ["num1", "num2", "combined"])

df.printSchema()


df2_original = spark.createDataFrame(
    [(50, 100, {"classification": "General", "score": .3493, "fv": "normal"}), (100, 250, {"classification": "outofbox", "score": .3435, "fv": "critical"})], ["num1", "num2", "combined"])
# df2_original.select("num1","num2",create_map("combined"))
df2_original.selectExpr("combined","num1","num2").show()


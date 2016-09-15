from pyspark.sql import SparkSession
from PIL import Image
import requests
from StringIO import StringIO
import numpy as np

spark = SparkSession \
    .builder \
    .appName("PythonSQL") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

url='http://weknowyourdreams.com/images/space/space-01.jpg'
response = requests.get(url)
img = Image.open(StringIO(response.content))

img = np.array(img)


for x in range(0, 10):
    row = [(x, img.tolist())]
    if x == 0:
        df = spark.createDataFrame(row)
    else:
        df = df.unionAll(spark.createDataFrame(row))
df.repartition(1).write.mode("overwrite").option("compression","gzip").save("/tmp/imagedf")


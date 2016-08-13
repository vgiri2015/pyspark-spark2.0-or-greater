import os
import sys
# Set the path for spark installation
# this is the path where you have built spark using sbt/sbt assembly
os.environ['SPARK_HOME'] = "/usr/local/Cellar/spark2.0_master/spark"

# Append to PYTHONPATH so that pyspark could be found
sys.path.append("/usr/local/Cellar/spark2.0_master/spark/python/")
sys.path.append("/usr/local/Cellar/spark2.0_master/spark/python/lib")
# sys.path.append("/home/jie/d2/spark-0.9.1/python")
# Now we are ready to import Spark Modules
try:
    from pyspark import SparkContext
    from pyspark import SparkConf
    print "Hey nice"
except ImportError as e:
    print ("Error importing Spark Modules", e)
sys.exit(1)


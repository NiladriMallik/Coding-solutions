from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import datetime

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(world):
    # DataFrame operations here
    return world.filter(
        (F.col('area') > 3000000) |
        (F.col("population") > 25000000)
    ).select(
        "name", "population", "area"
    ).orderBy("name")

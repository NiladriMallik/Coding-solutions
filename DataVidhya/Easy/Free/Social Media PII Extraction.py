from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(input_df):
    # Write code here
    output = input_df.select(
        F.concat(F.lit("******"), F.substring('phone', 7, 10)).alias('anon_phone'),
        F.split('email', '@').getItem(1).alias('email_domain'),
        F.col('user_id')
    ).orderBy('anon_phone')
    return output
    
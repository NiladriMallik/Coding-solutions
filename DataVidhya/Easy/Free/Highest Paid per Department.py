from pyspark.sql import functions as F
from pyspark.sql import Window as W
from pyspark.sql import SparkSession
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(input_df):
    window = W.partitionBy('department')

    output_df = input_df.withColumn(
        'largest_salary', F.max('salary').over(window)
    ).filter(
        F.col('salary') == F.col('largest_salary')
    ).select(
        'department',
        'largest_salary'
    )

    return output_df

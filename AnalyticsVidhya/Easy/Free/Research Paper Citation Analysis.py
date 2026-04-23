from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(authors, research_papers):
    # Write code here
    output = authors.join(
        research_papers,
        on = 'paper_id'
    )
    window = W.partitionBy('paper_id').orderBy('author_id')
    output = output.withColumn(
        'row_number', F.row_number().over(window)
    ).select(
        'author_id', 'name', 'paper_id', 'row_number'
    )
    return output

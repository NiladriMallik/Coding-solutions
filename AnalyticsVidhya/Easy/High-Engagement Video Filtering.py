from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(video_stream_df):
    return video_stream_df.filter(
        (F.col('view_count') > 1000000) &
        (F.year(F.current_date()) - F.col('release_year') < 9)
    ).orderBy(F.col('duration'))
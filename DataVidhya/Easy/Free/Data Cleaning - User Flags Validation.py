from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
import datetime

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(user_flags):
    # Your solution here
    output = user_flags.filter(
        (F.col('reason').isNotNull()) &
        (F.col('flag_type').isNotNull()) &
        (F.col('flag_type') != '') &
        (F.col('flag_type') != 'N/A') &
        (F.col('reason') != 'N/A')
    ).groupBy("user_id").agg(
        F.count("flag_id").alias("valid_flag_count")
    ).orderBy(
        F.desc('valid_flag_count'),
        F.asc('user_id')
    )
    return output

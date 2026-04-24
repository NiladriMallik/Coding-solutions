from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def etl(avow_sample):
    return avow_sample.filter(
        F.col('author_id') == F.col('viewer_id')
    ).select(
        F.col('author_id').alias('id')
    ).distinct().orderBy(
        'author_id'
    )

    
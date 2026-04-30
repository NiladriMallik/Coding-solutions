from pyspark.sql import SparkSession
from pyspark.sql.functions import month, avg, col

def etl(input_df):
    output = input_df.groupBy(
        'month', 'product_id'
    ).agg(F.avg('stars').alias('avg_stars'))\
    .select(
        'avg_stars',
        F.col('month').alias('mth'),
        F.col('product_id').alias('product'),
    )
    return output
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def etl(input_df):
    output_df = input_df.select(
        'Date', 'Differential', 'Result',
        F.concat_ws(' by ', F.col('Result'), F.col('Differential')).alias('Scoreline')
    )
    return output_df

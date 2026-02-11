# Import your libraries
import pandas as pd

fact_events.groupby(
    [fact_events['client_id'], fact_events['time_id'].dt.month]
    )['user_id'].nunique().reset_index()


# PySpark
import pyspark
from pyspark.sql import functions as F

result = fact_events\
.withColumn('month', F.month(F.col('time_id')))\
.groupBy(
    F.col('month'), F.col('client_id')
)\
.agg(
    F.countDistinct(F.col('user_id')).alias('users_num')
)\
.select('month', 'client_id', 'users_num')

result.toPandas()
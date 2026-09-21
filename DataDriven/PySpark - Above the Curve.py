from pyspark.sql import functions as F
from pyspark.sql import Window

global_window = Window.partitionBy()

results = transactions.groupBy(
    'user_id'
).agg(
    F.sum('total_amount').alias('total')
).withColumn(
    'global_avg',
    F.avg('total').over(global_window)
).filter(
    F.col('total') - F.col('global_avg') > 0
).withColumn(
    'above_avg',
    F.col('total') - F.col('global_avg')
).select(
    'user_id', 'total', 'above_avg'
).orderBy(
    F.col('total').desc()
)

results.show()
from pyspark.sql import functions as F
from pyspark.sql.window import Window

w = Window.partitionBy().orderBy(F.col('call_count').desc())

results = api_calls.filter(
    F.col('err_msg').isNotNull()
).withColumn(
    'time_segment',
    F.when(
        F.hour(F.col('call_time')) < 12, 'Morning'
    ).when(
        (F.hour(F.col('call_time')) >= 12) &
        (F.hour(F.col('call_time'))<= 15),
        'Early Afternoon'
    ).otherwise(
        'Late Afternoon'
    )
).groupBy(
    'status', 'time_segment'
).agg(
    F.count('*').alias('call_count')
).withColumn(
    'rank',
    F.dense_rank().over(w)
).filter(
    F.col('rank') <= 3
).orderBy(
    F.col('call_count').desc()
).select(
    'status', 'time_segment', 'call_count'
)

results.show()
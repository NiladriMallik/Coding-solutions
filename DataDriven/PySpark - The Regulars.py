from pyspark.sql import functions as F, Window

result = user_sessions.groupBy(
    'user_id'
).agg(
    F.count_distinct(F.month(F.col('session_start'))).alias('distinct_months')
).filter(
    F.col('distinct_months') > 2
).select('user_id')

result.show()

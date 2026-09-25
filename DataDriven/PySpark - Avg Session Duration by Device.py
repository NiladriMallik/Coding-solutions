from pyspark.sql import functions as F

results = user_sessions.join(
    devices,
    on='device_id',
    how='inner'
).groupBy(
    'device_type'
).agg(
    F.avg('session_duration_sec').alias('avg_session_duration')
).orderBy(
    F.col('device_type').asc()
)

results.show()
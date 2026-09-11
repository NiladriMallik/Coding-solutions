from pyspark.sql import functions as F

result = data_pipes.filter(
    F.col('start_at').isNotNull()
).groupBy(
    F.month('start_at').alias('month')
).agg(
    F.count('pipe_id').alias('pipeline_runs')
).orderBy(
    F.col('pipeline_runs').desc()
).limit(1)

result.show()

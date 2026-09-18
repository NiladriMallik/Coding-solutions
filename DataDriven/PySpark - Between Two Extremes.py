from pyspark.sql import functions as F

results = api_calls.groupBy().agg(
    F.min('latency').alias('min_latency'),
    F.max('latency').alias('max_latency'),
    (F.sum('latency') - F.max('latency') - F.min('latency')).alias('sum_between')
)

results.show()
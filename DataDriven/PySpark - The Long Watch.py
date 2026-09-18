from pyspark.sql import functions as F

results = content_items.groupBy(
    'content_type'
).agg(
    F.count('content_id').alias('items_published'),
    F.avg('duration_seconds').alias('avg_runtime')
).orderBy(
    F.col('avg_runtime').desc()
)

results.show()
from pyspark.sql import functions as F

results = content_items.filter(
    F.col('duration_seconds').isNotNull()
).select(
    'content_id',
    'content_type',
    'duration_seconds'
).join(
    content_views.filter(
        (F.col('viewed_at') >= '2026-01-01') &
        (F.col('viewed_at') < '2027-12-31')
    ).select(
        'content_id',
        'view_id',
        'watch_seconds'
    ),
    on='content_id'
).withColumn(
    'completion',
    F.col('watch_seconds').cast('float')/F.col('duration_seconds').cast('float')
).groupBy(
    'content_type'
).agg(
    F.count('view_id').alias('view_count'),
    F.avg('completion').alias('avg_completion_rate')
).orderBy(
    F.col('avg_completion_rate').desc()
).select(
    F.col('content_type').alias('content_format'), 'avg_completion_rate', 'view_count'
)

results.show()

from pyspark.sql import functions as F

results = users.filter(
    F.col('age_bucket').isNotNull()
).select(
    'user_id', 'age_bucket'
).join(
    ad_impressions.select(
        'user_id', 'revenue'
    ),
    on='user_id'
).groupBy(
    'age_bucket'
).agg(
    F.sum('revenue').alias('total_revenue')
).orderBy(
    F.col('total_revenue').desc()
)

results.show()
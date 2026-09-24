from pyspark.sql import functions as F

results = code_reviews.filter(
    F.col('merged').isNotNull()
).groupBy(
    'reviewer'
).agg(
    F.count('*').alias('review_count')
).filter(
    F.col('review_count') > 24
).orderBy(
    F.col('review_count').desc()
)

results.show()
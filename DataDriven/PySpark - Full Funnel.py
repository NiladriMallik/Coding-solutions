from pyspark.sql import functions as F

results = users.join(
    search_queries,
    how='left',
    on='user_id'
).join(
    page_views,
    on='user_id',
    how='left'
).join(
    transactions,
    on='user_id',
    how='left'
).filter(
    (F.col('query_id').isNotNull()) &
    (F.col('view_id').isNotNull()) &
    (F.col('transaction_id').isNotNull())
).select(
    'username'
).distinct().orderBy(
    F.col('username').asc()
)

results.show()
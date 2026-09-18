from pyspark.sql import functions as F

results = users.select(
    'user_id', 'username'
).join(
    transactions.select(
        'user_id', 'product_id', 'total_amount'
    ).filter(
        F.col('quantity') > 0
    ),
    on='user_id'
).groupBy(
    'user_id', 'username'
).agg(
    F.count_distinct('product_id').alias('distinct_products'),
    F.sum('total_amount').alias('total_spend')
).filter(
    F.col('distinct_products') > 5
).select('username', 'distinct_products', 'total_spend')
results.show()

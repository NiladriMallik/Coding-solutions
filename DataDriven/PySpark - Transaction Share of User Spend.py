from pyspark.sql import functions as F
from pyspark.sql.window import Window

w = Window.partitionBy('user_id', 'username')

results = users.select(
    'user_id','username'
).join(
    transactions.select(
        'transaction_id', 'user_id', F.col('total_amount').cast('float').alias('total_amount'), 'transaction_date'
    ),
    on='user_id'
).withColumn(
    'total_spend',
    F.sum('total_amount').over(w)
).withColumn(
    'spend_share',
    F.col('total_amount') / F.col('total_spend')
).orderBy(
    F.col('transaction_date').asc()
).select(
    'transaction_id', 'username', 'total_amount', 'spend_share'
)

results.show()

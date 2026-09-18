from pyspark.sql import functions as F
from pyspark.sql.window import Window

w = Window.over()

results = orders.groupBy(
    'region'
).agg(
    F.count("order_id").alias('order_count')
).orderBy(
    F.col('order_count').desc(), 'region'
).limit(1)

results.show()

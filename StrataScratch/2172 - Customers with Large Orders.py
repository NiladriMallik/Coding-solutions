import pyspark
from pyspark.sql import functions as F

output = online_store_customers.join(online_store_orders,
    on = 'customer_id',
    how = 'left'
).filter(
    F.col('amount') > 100
).select('customer_id', 'customer_name').distinct()

output.toPandas()
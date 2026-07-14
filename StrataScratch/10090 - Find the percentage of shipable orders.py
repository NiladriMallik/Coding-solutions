# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
result = orders.join(
    customers,
    on = orders['cust_id'] == customers['id']
).withColumn(
    'address_known',
    F.when(F.col('address').isNotNull(), 1).otherwise(0)
).agg(
    F.sum('address_known').alias('address_known'),
    F.count('cust_id').alias('address_not_known')
).withColumn(
    'shipable_orders',
    (F.col('address_known') / F.col('address_not_known')) * 100
).select('shipable_orders')

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()

########################################################################################

# Cleaner optimized solution

result = orders.join(
    customers,
    on = orders['cust_id'] == customers['id'],
    how = 'left'
).agg(
    (
        F.avg(
            F.when(F.col('address').isNotNull(), 1).otherwise(0)
        ) * 100
    ).alias('shipable_orders')
)
result.toPandas()
# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = customers.join(
    orders,
    customers['id'] == orders['cust_id']
).groupBy(
    'cust_id', 'first_name'
).agg(
    F.sum('total_order_cost').alias('total_order_cost')
).orderBy('first_name', ascending=True)

output.toPandas()
# PySpark

# Import your libraries
import pyspark
from pyspark.sql import functions as F
from pyspark.sql import Window

window = Window.partitionBy('user_id').orderBy('created_at')

# Start writing code
output = amazon_transactions.select(
    'user_id',
    'created_at',
    F.row_number().over(window).alias('order_id'),
    F.lag('created_at', 1).over(window).alias('previous_order_date')
).filter(
    (F.datediff(F.col('created_at'), F.col('previous_order_date')) <= 7) &
    (F.datediff(F.col('created_at'), F.col('previous_order_date')) > 0) &
    (F.col('order_id') == 2)
).select('user_id')

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()


# Optimized

output = amazon_transactions.withColumns({
    'previous_order_date': F.lag('created_at', 1).over(window),
    'order_id': F.row_number().over(window)
}).filter(
    F.datediff(F.col('created_at'), F.col('previous_order_date')).between(1, 7) &
    (F.col('order_id') == 2)
).select('user_id').distinct()
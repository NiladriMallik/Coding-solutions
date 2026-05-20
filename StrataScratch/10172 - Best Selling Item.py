# Import your libraries
import pyspark
from pyspark.sql import functions as F
from pyspark.sql import Window

window = Window().partitionBy('month').orderBy(F.desc('total_paid'))

# Start writing code
output = online_retail.filter(
    F.col('quantity') > 0
).groupBy(
    F.month('invoicedate').alias('month'), 'description'
).agg(
    F.sum(F.col('unitprice') * F.col('quantity')).alias('total_paid')
).withColumn(
    'row_number',
    F.row_number().over(window)
).filter(
    F.col('row_number') == 1
).select(
    'month', 'description', 'total_paid'
)

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
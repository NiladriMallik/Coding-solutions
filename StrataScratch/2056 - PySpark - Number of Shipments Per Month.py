# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = amazon_shipment.withColumn(
    'unique_id', F.concat(F.col('shipment_id'), F.col('sub_id'))
).withColumn(
    'year_month', F.date_format(F.col('shipment_date'), 'yyyy-MM')
).groupBy('year_month').agg(
    F.count('unique_id').alias('shipment_count')
)

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
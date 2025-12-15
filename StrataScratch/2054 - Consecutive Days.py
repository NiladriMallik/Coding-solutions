# PySpark
# Import your libraries
import pyspark
from pyspark.sql.functions import *
from pyspark.sql.window import Window

window = Window.partitionBy('user_id').orderBy('record_date')

# Start writing code
sf_events = (
    sf_events.select(
        col('user_id'),
        col('record_date')
    ).withColumn('day2', lead('record_date').over(window))\
    .withColumn('day3', lead('record_date', 2).over(window))
    .filter(
        (date_add(col('record_date'), 1) == col('day2')) &
        (date_add(col('record_date'), 2) == col('day3'))
    ).select('user_id')
)

# To validate your solution, convert your final pySpark df to a pandas df
sf_events.toPandas()
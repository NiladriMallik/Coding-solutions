# Import your libraries
import pyspark
from pyspark.sql import Window
from pyspark.sql import functions as F

window_spec = (
    Window
    .partitionBy('cust_id')
    .orderBy('timestamp')
)

cust_tracking = cust_tracking.withColumn(
    "prev_timestamp",
    F.lag('timestamp', 1).over(window_spec)
).withColumn(
    "hours",
    F.when(
        F.col("state") == 0,
        (F.unix_timestamp("timestamp") - F.unix_timestamp("prev_timestamp")) / 60.0
    ).otherwise(0)
).groupBy("cust_id", "state", 'timestamp')\
    .agg(
        (F.sum("hours")/60.0).alias("hours")
    ).groupBy('cust_id')\
        .agg(
            (F.sum('hours')).alias('total_time')
        ).orderBy('cust_id')

# To validate your solution, convert your final pySpark df to a pandas df
cust_tracking.toPandas()
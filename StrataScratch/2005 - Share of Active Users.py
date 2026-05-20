# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = fb_active_users.select(
    (
        F.sum(
            F.when(
                (F.col('country') == 'USA') &
                (F.col('status') == 'open'),
                1
            ).otherwise(0)  
        ) * 100 / F.count("*")
    ).alias('us_active_share')
)

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
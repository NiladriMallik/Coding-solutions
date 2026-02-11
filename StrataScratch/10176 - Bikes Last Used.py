# Import your libraries
import pandas as pd

# Start writing code
df_grouped = dc_bikeshare_q1_2012\
                .groupby('bike_number')['end_time']\
                .max()\
                .reset_index()\
                .sort_values(by = 'end_time', ascending = False)
                
df_grouped


# PySpark
import pyspark
from pyspark.sql import functions as F

dc_bikeshare_q1_2012.groupBy('bike_number').agg(
    F.max('end_time').alias('last_used')
).toPandas()
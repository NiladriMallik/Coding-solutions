# Import your libraries
import pandas as pd

# Start writing code
grouped_df = facebook_employees\
                .merge(facebook_hack_survey,left_on = 'id',right_on = 'employee_id')\
                .groupby('location')['popularity']\
                .mean()\
                .reset_index()
grouped_df.head()

# PySpark
import pyspark
from pyspark.sql import functions as F

popularity = facebook_employees.join(
    facebook_hack_survey,
    on = facebook_hack_survey['employee_id'] == facebook_employees['id'],
    how = 'inner'
)\
.groupBy('location')\
.agg(
    F.mean('popularity').alias('popularity')
)


popularity.toPandas()
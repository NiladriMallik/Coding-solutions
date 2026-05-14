# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = airbnb_hosts.join(
    airbnb_units, on = 'host_id'
).filter(
   ( F.col('age') < 30) &
   (F.col('unit_type') == 'Apartment')
).distinct().groupBy('nationality').agg(F.count('*'))

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
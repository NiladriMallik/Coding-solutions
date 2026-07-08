# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = los_angeles_restaurant_health_inspections.filter(
    (F.col('facility_name') == 'STREET CHURROS') &
    (F.col('score') < 95)
).select('activity_date', 'pe_description')

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
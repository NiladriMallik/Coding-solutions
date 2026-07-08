# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
result = sf_restaurant_health_violations.filter(
    F.col('business_name') == 'Roxanne Cafe'
).groupBy(
    F.year(F.col('inspection_date')).alias('year')
).agg(
    F.count('inspection_id').alias('inspection_count')
).orderBy(F.col('year').asc())

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()
# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
result = lyft_drivers.filter(
    (F.col('yearly_salary') >= 70000) |
    (F.col('yearly_salary') <= 30000)
)

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()
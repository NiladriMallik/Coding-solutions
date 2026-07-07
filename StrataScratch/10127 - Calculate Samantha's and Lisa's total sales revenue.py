# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
result = sales_performance.filter(
    (F.col('salesperson') == 'Samantha') |
    (F.col('salesperson') == 'Lisa')
).agg(F.sum('sales_revenue'))

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()
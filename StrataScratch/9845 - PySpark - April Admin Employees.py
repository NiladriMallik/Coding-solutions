# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
result = worker.filter(
    (F.col('department') == 'Admin') &
    (F.month(F.col('joining_date')) >= 4)
).agg(F.count('worker_id').alias('n_admins'))

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()
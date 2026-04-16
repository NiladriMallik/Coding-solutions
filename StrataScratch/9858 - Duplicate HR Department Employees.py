import pyspark
from pyspark.sql import functions as F

output = worker.filter(
    F.col('department') == 'HR'
).select('first_name', 'department')

output = output.union(output)

output.toPandas()
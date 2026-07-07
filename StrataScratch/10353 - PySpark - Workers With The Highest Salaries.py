# Import your libraries
import pyspark
from pyspark.sql import Window, functions as F

# Start writing code
result = worker.join(
    title,
    worker['worker_id'] == title['worker_ref_id'],
    how = 'inner',
).orderBy(F.col('salary').desc())

max_salary = result.select(F.max('salary')).first()[0]

result = result.filter(F.col('salary') == max_salary).select('worker_title')

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()
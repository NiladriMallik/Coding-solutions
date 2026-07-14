# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = sf_employee.join(
    sf_bonus.groupBy('worker_ref_id').agg(F.sum('bonus').alias('bonus')),
    sf_employee['id'] == sf_bonus['worker_ref_id'],
    how = 'right'
).groupBy('employee_title', 'sex').agg(
    F.avg(F.col('bonus') + F.col('salary'))
)

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
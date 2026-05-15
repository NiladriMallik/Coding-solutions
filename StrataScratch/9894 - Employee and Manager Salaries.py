# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = employee.select(
    F.col('id').alias('manager_id'),
    F.col('salary').alias('manager_salary')
).join(
    employee,
    on = 'manager_id'
).filter(
    F.col('salary') > F.col('manager_salary')
).select('first_name', 'salary')

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
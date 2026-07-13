# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
highest_target = salesforce_employees.filter(
    F.col('manager_id') == 13
).orderBy(F.col('target').desc()).first()['target']

output = salesforce_employees.filter(
    (F.col('manager_id') == 13) &
    (F.col('target') == highest_target)
).select('first_name', 'target')

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
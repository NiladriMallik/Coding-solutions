Highest Salary In Department# Import your libraries
import pyspark
from pyspark.sql import functions as F
from pyspark.sql import Window

window = Window().partitionBy('department').orderBy(F.col('salary').desc())

# Start writing code
output = employee.withColumn(
    'row_num', F.row_number().over(window)
).filter(F.col('row_num') == 1).select(
    'department', 'first_name', 'salary'
)

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
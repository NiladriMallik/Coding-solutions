# Import your libraries
import pyspark
from pyspark.sql import functions as F
from pyspark.sql import Window

window = Window().orderBy(F.desc('salary'))

# Start writing code
output = employee.withColumn(
    'rank', F.rank().over(window)
).filter(F.col('rank') == 2).select('salary')

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()


# Optimized code without Window function
output = employee.orderBy(
    F.desc("salary")
).limit(2).orderBy(
    F.asc('salary')
).limit(1).select('salary')

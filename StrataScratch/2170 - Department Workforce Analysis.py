import pyspark
from pyspark.sql import functions as F
from pyspark.sql import Window

dept_window = Window.partitionBy('department')

output = techcorp_workforce.filter(
    F.year(F.col('joining_date')) > 2020
).withColumn(
    'emp_count', F.count('department').over(dept_window)
).filter(
    F.col('emp_count') > 4
).groupBy('department', 'emp_count').agg(
    F.sum('salary').alias('total_payroll'),
    F.avg('salary').alias('average_salary'),
).withColumnRenamed(
    'emp_count', 'headcount'
)

output.toPandas()

###################################################################

# Highly optimized and better code
# Import your libraries
import pyspark
from pyspark.sql import functions as F
from pyspark.sql import Window

output = techcorp_workforce.filter(
    F.year(F.col('joining_date')) > 2020
).groupBy(
    F.col('department')
).agg(
    F.count("id").alias('headcount'),
    F.sum('salary').alias('total_payroll'),
    F.avg('salary').alias('average_salary')
).filter(
    F.col('headcount') > 4
)

output.toPandas()

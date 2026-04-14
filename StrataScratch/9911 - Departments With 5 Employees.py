import pyspark
import pyspark.sql.functions as F

output = employee.groupBy('department').agg(
    F.count('id').alias('employee_count')
).filter(
    F.col('employee_count') >= 5
).select("department")

output.toPandas()
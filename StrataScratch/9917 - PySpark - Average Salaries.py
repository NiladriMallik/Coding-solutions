import pyspark
from pyspark.sql import functions as F

dept_wise_avg_salary = employee.groupBy(
    'department'
).agg(F.avg('salary').alias('avg_salary'))

result = employee.join(
    dept_wise_avg_salary,
    on='department'
).select(
    'department',
    'first_name',
    'salary',
    'avg_salary'
)

result.toPandas()
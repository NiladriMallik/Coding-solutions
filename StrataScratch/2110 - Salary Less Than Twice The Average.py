import pyspark
from pyspark.sql import functions as F

manager_salaries = map_employee_hierarchy.join(
    dim_employee,
    dim_employee['empl_id'] == map_employee_hierarchy['manager_empl_id']
).select(
    F.col('manager_empl_id'),
    F.col('salary').alias('manager_salary')
)

output = dim_employee.join(
    map_employee_hierarchy,
    on = 'empl_id'
).select(
    F.col('empl_id'),
    F.col('salary').alias('empl_salary'),
    F.col('manager_empl_id')
)

output = output.join(
    manager_salaries,
    on = 'manager_empl_id'
).select(
    'manager_empl_id', 'manager_salary', 'empl_salary'
).groupBy('manager_empl_id', 'manager_salary').agg(
    F.avg(F.col('empl_salary')).alias('avg_reportee_salaries')
).filter(
    F.col('manager_salary') < 2 * F.col('avg_reportee_salaries')
)

output.toPandas()
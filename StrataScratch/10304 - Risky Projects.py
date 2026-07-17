# Import your libraries
import pyspark
from pyspark.sql import functions as F

linkedin_projects = linkedin_projects.alias('lp')
linkedin_emp_projects = linkedin_emp_projects.alias('lep')
linkedin_employees = linkedin_employees.alias('le')

# Start writing code
output = linkedin_employees.join(
    linkedin_emp_projects,
    F.col('lep.emp_id') == F.col('le.id'),
    how = 'left'
).join(
    linkedin_projects,
    F.col('lp.id') == F.col('lep.project_id'),
    how = 'left'
).groupBy(
    F.col('lp.title'),
    F.col('lp.budget'),
    F.col('lp.start_date'),
    F.col('lp.end_date')
).agg(
    F.ceil(
        F.sum(
            F.col('le.salary') / 365.0 * F.datediff(
                    F.col('lp.end_date'),
                    F.col('lp.start_date')
            )
        )
    ).alias('prorated_employee_expense')
).filter(
    F.col('lp.budget') < F.col('prorated_employee_expense')
).select('title', 'budget', 'prorated_employee_expense')


# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
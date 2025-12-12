# Import your libraries
import pandas as pd

ms_employee_salary.head()

ms_employee_salary.groupby(['id', 'first_name', 'last_name', 'department_id'], as_index = False)['salary'].max().sort_values(by = 'id')

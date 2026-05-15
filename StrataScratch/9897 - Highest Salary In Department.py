# Import your libraries
import pandas as pd

# Start writing code
max_salaries = employee.groupby('department')['salary'].max().reset_index()

result = pd.merge(
    employee[['first_name', 'department', 'salary']],
    max_salaries,
    on = ['department', 'salary'],
    how = 'inner'
)
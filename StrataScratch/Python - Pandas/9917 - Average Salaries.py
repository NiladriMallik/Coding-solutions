# Import your libraries
import pandas as pd

# Start writing code
grouped_df = employee\
            .groupby('department')['salary']\
            .mean()\
            .reset_index(name = 'avg_salary')\
            .merge(employee, on = 'department')[['department', 'first_name', 'salary', 'avg_salary']]
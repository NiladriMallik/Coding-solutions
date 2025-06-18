# Import your libraries
import pandas as pd

# Start writing code
db_grouped = db_employee\
            .merge(db_dept, left_on = 'department_id', right_on = 'id')\
            .groupby('department')['salary']\
            .max()

abs(db_grouped.loc['engineering'] - db_grouped.loc['marketing'])
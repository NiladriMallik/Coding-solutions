# Import your libraries
import pandas as pd

# Start writing code
worker[(worker['department'] == 'Admin') & (worker['joining_date'].dt.month.astype(int) >= 4)]['department'].count()

result = pd.DataFrame({'n_admins' : [4]})
result.head()
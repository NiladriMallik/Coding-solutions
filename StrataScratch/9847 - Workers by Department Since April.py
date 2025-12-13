# Import your libraries
import pandas as pd

# Start writing code
worker[worker['joining_date'] >= '2014-04-1']\
.groupby('department')['worker_id']\
.count()\
.reset_index(name = 'worker_count')\
.sort_values(by = 'worker_count', ascending = False)
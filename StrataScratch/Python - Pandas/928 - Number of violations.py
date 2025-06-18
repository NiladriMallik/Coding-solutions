# Import your libraries
import pandas as pd

# Start writing code
sf_restaurant_health_violations[sf_restaurant_health_violations['business_name'] == 'Roxanne Cafe']\
.assign(inspection_year = pd.to_datetime(sf_restaurant_health_violations['inspection_date']).dt.year)\
.groupby('inspection_year')['violation_id']\
.count()\
.reset_index(name = 'n_violations')\
.sort_values('inspection_year')
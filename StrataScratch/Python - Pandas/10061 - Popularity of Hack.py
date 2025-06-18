# Import your libraries
import pandas as pd

# Start writing code
grouped_df = facebook_employees\
                .merge(facebook_hack_survey,left_on = 'id',right_on = 'employee_id')\
                .groupby('location')['popularity']\
                .mean()\
                .reset_index()
grouped_df.head()
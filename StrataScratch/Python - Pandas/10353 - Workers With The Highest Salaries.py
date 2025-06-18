# Import your libraries
import pandas as pd

# Start writing code
worker.head()

merged_df = worker.merge(title,
            left_on = 'worker_id', right_on = 'worker_ref_id'
            )
merged_df = merged_df.loc[merged_df['salary'].eq(merged_df['salary'].max()), 'worker_title']
# Import your libraries
import pandas as pd

fact_events.groupby(
    [fact_events['client_id'], fact_events['time_id'].dt.month]
    )['user_id'].nunique().reset_index()
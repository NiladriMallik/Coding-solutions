# Import your libraries
import pandas as pd

# Start writing code
playbook_events[playbook_events['device'] == 'macbook pro']\
.groupby('event_name')\
.size()\
.reset_index(name = 'event_count')\
.sort_values(by = 'event_count', ascending = False)
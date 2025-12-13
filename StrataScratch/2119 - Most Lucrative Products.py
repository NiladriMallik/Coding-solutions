# Import your libraries
import pandas as pd

# Start writing code

online_orders['revenue'] = online_orders['cost_in_dollars'] * online_orders['units_sold']
online_orders.groupby('product_id')['revenue'] \
    .sum() \
    .sort_values(ascending = False) \
    .reset_index() \
    .head()
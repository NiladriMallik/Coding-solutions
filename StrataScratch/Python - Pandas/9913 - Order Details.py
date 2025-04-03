# Import your libraries
import pandas as pd

customers[customers['first_name'].isin(['Jill','Eva'])].\
    merge(orders, left_on = 'id', right_on = 'cust_id').\
    sort_values(by = 'cust_id')\
    [['first_name', 'order_date', 'order_details', 'total_order_cost']]
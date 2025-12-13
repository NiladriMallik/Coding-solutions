# Import your libraries
import pandas as pd

# Start writing code
# amazon_shipment.head()

amazon_shipment.groupby(
    [amazon_shipment['shipment_date'].dt.strftime("%Y-%m")]
    )['shipment_id', 'sub_id'].size().reset_index(name = 'count')
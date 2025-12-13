# Import your libraries
import pandas as pd

# airbnb_search_details.head()
# Start writing code
airbnb_search_details.groupby(['city', 'property_type'], 
    as_index=False)[['bathrooms', 'bedrooms']].mean()

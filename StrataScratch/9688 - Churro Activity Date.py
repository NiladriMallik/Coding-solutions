# Import your libraries
import pandas as pd
los_angeles_restaurant_health_inspections.head()
# Start writing code
los_angeles_restaurant_health_inspections['activity_date'] = los_angeles_restaurant_health_inspections['activity_date'].dt.date

los_angeles_restaurant_health_inspections.loc[
    (los_angeles_restaurant_health_inspections['score'] < 95) & 
    (los_angeles_restaurant_health_inspections['facility_name'] == 'STREET CHURROS')
    ][['activity_date', 'pe_description']]
# Import your libraries
import pyspark

# Start writing code
output = airbnb_hosts.join(
    airbnb_guests,
    (airbnb_guests['gender'] == airbnb_hosts['gender']) &
    (airbnb_hosts['nationality'] == airbnb_guests['nationality'])
).select('host_id', 'guest_id').distinct()

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
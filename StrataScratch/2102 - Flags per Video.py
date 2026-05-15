# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = user_flags.filter(
    F.col('flag_id').isNotNull()
).fillna({
    "user_firstname": "NoUserFirstName",
    "user_lastname": 'NoUserLastName'
}).groupBy('video_id').agg(
    F.countDistinct('user_firstname', 'user_lastname').alias('flags_count')
)
# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
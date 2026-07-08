# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
result = playbook_events.filter(
    F.col('device') == 'macbook pro'
).groupBy('event_name').agg(
    F.count('user_id').alias('event_count')
).orderBy(F.col('event_count').desc())

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()
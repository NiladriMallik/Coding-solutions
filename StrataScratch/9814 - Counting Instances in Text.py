# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = google_file_store.withColumn(
    'words', F.explode(F.split(F.col('contents'), " "))
).filter(
    F.col('words').isin(['bull', 'bear'])
).groupBy('words').agg(
    F.count('words').alias('count')
)

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
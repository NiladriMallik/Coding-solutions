# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = google_file_store.withColumn(
    'words',
    F.explode(F.split(F.col('contents'), ' '))
).withColumn(
   "words", F.lower(F.translate(F.col("words"), ".,", ""))
).groupBy('words').agg(
    F.count("*").alias("occurrences")
).orderBy(F.col("occurrences").desc())

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()

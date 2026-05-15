# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = facebook_complaints.groupBy('type').agg(
    F.sum(F.col('processed').cast('int')) / F.count("*")
)

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
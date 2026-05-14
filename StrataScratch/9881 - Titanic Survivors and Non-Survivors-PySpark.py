# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = titanic.groupBy(
    'survived'
).pivot('pclass').agg(
    F.count("*")
)

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
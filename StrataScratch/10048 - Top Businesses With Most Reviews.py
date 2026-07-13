# Import your libraries
import pyspark
from pyspark.sql import functions as F, Window

window = Window.orderBy(F.col('review_count').desc())

# Start writing code
output = yelp_business.withColumn(
    'rank', F.rank().over(window)
).filter(
    F.col('rank') <= 5
).select(
    'name', 'review_count'
).orderBy(
    F.col('rank').asc()
)

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
highest_votes = yelp_reviews.orderBy(
    F.col('cool').desc()
).limit(1).first()['cool']

result = yelp_reviews.filter(
    F.col('cool') == highest_votes
).select('business_name', 'review_text')
# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()


#################################################################################

# Alternate solution
result = yelp_reviews.filter(
    F.col('cool') == yelp_reviews.select(F.max('cool')).collect()[0][0]
).select('business_name', 'review_text')
# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()
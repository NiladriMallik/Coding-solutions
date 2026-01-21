# pyspark
# Import your libraries
import pyspark
from pyspark.sql import functions as F

result = (
    oscar_nominees
    .join(nominee_information, on = 'id', how = 'inner')
    .filter(F.col('winner') == 'FALSE')
    .groupBy("top_genre")
    .agg(F.count("*").alias("total_winnings"))
    .orderBy(F.desc("total_winnings"))
    .select('top_genre')
    .limit(1)
)

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()
# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
result = spotify_worldwide_daily_song_ranking.groupBy(
    'artist'
).agg(
    F.count('id').alias('count')
).orderBy(F.col('count').desc())

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()
# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = billboard_top_100_year_end.filter(
    (F.col('year') == 2010) &
    (F.col('year_rank') <= 10)
).orderBy('year_rank', ascending = True).select(
    "year_rank", "group_name", "song_name"
).distinct()

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
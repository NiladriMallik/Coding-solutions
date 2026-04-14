import pyspark
import pyspark.sql.functions as F

output = olympics_athletes_events.agg(
    F.min('age').alias('lowest_age'),
    F.avg('age').alias('mean_age'),
    F.max('age').alias('highest_age'),
)

output.toPandas()
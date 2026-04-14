import pyspark
import pyspark.sql.functions as F

output = olympics_athletes_events.filter(
    (F.col('age') > 40) &
    (F.col('medal').isin('Bronze', 'Silver'))
).select('name')

output.toPandas()
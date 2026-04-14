import pyspark
from pyspark.sql import functions as F

# Start writing code
output = lyft_rides.filter(
    (F.col('weather') == 'rainy') &
    (F.col('hour') < 12)
)

output.toPandas()
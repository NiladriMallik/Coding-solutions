import pyspark
from pyspark.sql import functions as F

output = lyft_rides.orderBy(F.col('gasoline_cost').desc()).limit(1).select('hour')

output.toPandas()

##########################################################################################

import pyspark
from pyspark.sql import functions as F

output = lyft_rides.where(
    F.col('gasoline_cost') == lyft_rides.agg(F.max('gasoline_cost')).first()[0]
).select('hour')

output.toPandas()
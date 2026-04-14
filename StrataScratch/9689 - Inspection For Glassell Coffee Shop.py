import pyspark
import pyspark.sql.functions as F

output = los_angeles_restaurant_health_inspections.filter(
    F.col('owner_name') == 'GLASSELL COFFEE SHOP LLC'
)

output.toPandas()
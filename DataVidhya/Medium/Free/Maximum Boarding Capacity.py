from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window

def etl(mcb_sample):
    window = Window.orderBy('boarding_order').rowsBetween(
        Window.unboundedPreceding,
        Window.currentRow
    )

    output = mcb_sample.withColumn(
        'cumulative_weight',
        F.sum('weight_kg').over(window.orderBy('boarding_order'))
    ).filter(
        F.col('cumulative_weight') <= 1000
    ).orderBy(
        F.desc('boarding_order')
    ).limit(1).select('passenger_name')
    return output

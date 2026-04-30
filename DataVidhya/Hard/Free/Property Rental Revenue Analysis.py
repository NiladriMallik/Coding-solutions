from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(prop_landlords, prop_properties):
    # Write code here
    output = prop_properties.join(
        prop_landlords,
        on = 'landlord_id',
        how = 'inner'
    ).withColumn(
        'landlord_name',
        F.concat_ws(' ', 'first_name', 'last_name')
    ).groupBy(
        'landlord_id', 'landlord_name'
    ).agg(
        F.sum('rent').alias('total_rental_income')
    )
    return output

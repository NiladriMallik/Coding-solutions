from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(customers, orders, products):
    # Write code here
    output = orders.join(
        customers,
        on = 'customer_id',
        how = 'left'
    ).join(
        products,
        on = 'product_id',
        how = 'left'
    ).select(
        F.col('email').alias('customer_email'),
        F.concat_ws(' ',F.col('first_name'), F.col('last_name')).alias('customer_name'),
        'order_date',
        'order_id',
        F.col('category').alias('product_category'),
        'product_name'
    )
    return output

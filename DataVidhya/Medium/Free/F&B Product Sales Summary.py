from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(inventory, products, sales):
    output = products.join(
        inventory,
        on = 'product_id',
        how = 'left'
    ).join(
        sales,
        on = 'product_id',
        how = 'left'
    ).select(
        'category',
        'name',
        'product_id',
        'quantity',
        'revenue',
        'stock'
    ).groupBy(
        'product_id', 'name', 'category'
    ).agg(
        F.sum('quantity').alias('total_quantity'),
        F.sum('revenue').alias('total_revenue'),
        F.first('stock').alias('total_stock')
    ).fillna(0,
             subset = ['total_quantity', 'total_revenue']
    ).orderBy(
        F.asc('category'), F.desc('total_stock')
    )
    return output

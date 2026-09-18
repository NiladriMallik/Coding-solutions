from pyspark.sql import functions as F
from pyspark.sql.window import Window

w = Window.partitionBy()

results = products.withColumn(
    'catalog_avg',
    F.avg('price').over(w)
).filter(
    F.col('price') > F.col('catalog_avg')
).select(
    'product_name',
    'category',
    'price',
    'catalog_avg'
)

results.show()
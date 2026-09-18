from pyspark.sql import functions as F
from pyspark.sql.window import Window

w = Window.orderBy(F.floor('rating').desc())

results = products.filter(
    F.col('rating').isNotNull()
).withColumn(
    'position',
    F.dense_rank().over(w)
).select(
    'product_name', 'category', 'rating', 'position'
)

results.show()

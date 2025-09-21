from pyspark.sql.functions import *

products_df = products_df.withColumn('Category',
                                     when(col('price') < 100, 'Low Price')\
                                     .otherwise(
                                         when((col('price') >= 100) & (col('price') <= 500), 'Medium Price')\
                                         .otherwise('High Price')
                                     )
                                     )

products_df.groupBy("Category") \
    .agg(count("*").alias("Product_Count")) \
    .sort(col("Product_Count").desc()) \
    .show()
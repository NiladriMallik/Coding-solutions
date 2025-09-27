from pyspark.sql import functions as F

#products_df.show(truncate=False)
#sales_df.show(truncate=False)

products_df.join(sales_df,
                 products_df.product_id == sales_df.product_id,
                 how = 'left'
                )\
                    .groupBy('product_name')\
                        .agg(
                            F.sum(F.col('price') * F.col('quantity'))\
                                .alias('total_sale_quantity'))\
                                    .sort(F.col('product_name').asc())\
                                        .show()

from pyspark.sql import functions as F

sales_df\
    .filter(
        (F.col('order_date').like('2022-02%')) &
        (
            (F.date_format(F.col('order_date'), 'EEEE') != 'Saturday') &
            (F.date_format(F.col('order_date'), 'EEEE') != 'Sunday')
        )
)\
    .groupBy('category')\
        .agg(F.sum('amount').alias('total_sales'))\
            .sort(F.col('total_sales').asc())\
                .show()
from pyspark.sql import functions as F

sales_df.groupBy('category').agg(
    F.sum(F.col('amount')).alias('SumOfSales')
    )\
    .filter(
        (F.col('order_date').like('2022-02%')) &
        (
            (F.format(F.col('order_date'), 'EEEE') != 'Saturday') &
            (F.format(F.col('order_date'), 'EEEE') != 'Sunday')
        )
).show()
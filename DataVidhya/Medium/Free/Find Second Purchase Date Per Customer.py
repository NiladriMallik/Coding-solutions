from pyspark.sql import functions as F
from pyspark.sql.window import Window

order_window = Window.partitionBy('customer_id').orderBy(
    F.col('order_date').asc()
)

def etl(orders):
    output = orders.withColumn({
        'order_num', F.row_number().over(order_window),
        'previous_date', F.lag('order_date', 1).over(order_window)
    }).withColumn(
        'metric', F.datediff(F.col('order_date'), F.col('previous_date'))
    ).filter(
        F.col('order_num') == 2
    ).select(
        F.col('customer_id').alias('id'),
        'metric',
        F.col('amount').alias('result_value')
    )

    return output

# Optimized

def etl(orders):
    output = orders.select(
        F.col('customer_id').alias('id'),
        F.col('amount').alias('result_value'),
        F.row_number().over(order_window).alias('order_num'),
        F.datediff(
            F.col('order_date'),
            F.lag('order_date', 1).over(order_window)
        ).alias('metric')
    )

    return output.filter(F.col('order_num') == 2).drop('order_num')
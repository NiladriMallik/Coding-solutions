from pyspark.sql import functions as F
from pyspark.sql.window import Window

window = Window.partitionBy('customer_id').orderBy('transaction_date')

def etl(transactions):
    output = transactions.select(
        'amount',
        'customer_id',
        F.row_number().over(window).alias('row_num'),
        'transaction_id'
    ).filter(
        F.col('row_num') == 3
    )

    return output

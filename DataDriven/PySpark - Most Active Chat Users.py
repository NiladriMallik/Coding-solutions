from pyspark.sql import functions as F, Window

window = Window.orderBy(F.col('total_messages').desc())

result = chat_msgs.groupBy(
    'sender_id'
).agg(
    F.count('msg_id').alias('total_messages')
).select(
    F.dense_rank().over(window).alias('rank'),
    'sender_id',
    'total_messages'
).orderBy(
    F.col('total_messages').desc()
)

result.show()
import pyspark
import pyspark.sql.functions as F

output = fintech_app_users.filter(
    F.col('phone_number').isNull()
).select('user_id', 'user_name')

output.toPandas()
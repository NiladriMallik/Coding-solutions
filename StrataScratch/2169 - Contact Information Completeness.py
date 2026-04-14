import pyspark
import pyspark.sql.functions as F

output = techcorp_workforce.agg(
    (
        F.sum(F.when(F.col('phone_number').isNull(), 1).otherwise(0))/
        F.count('*')
    ).alias('ratio')
)

output.toPandas()
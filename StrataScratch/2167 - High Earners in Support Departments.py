import pyspark
import pyspark.sql.functions as F

output = techcorp_workforce.filter(
    (F.col('salary') > 80000) &
    (F.col('department').isin('HR', 'Admin'))
).select('first_name', 'last_name', 'department', 'salary')

output.toPandas()
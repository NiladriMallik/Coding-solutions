import pyspark
import pyspark.sql.functions as F

output = worker.filter(
    (F.col('first_name').endswith('h')) &
    (F.length(F.col('first_name')) == 6)
)

output.toPandas()
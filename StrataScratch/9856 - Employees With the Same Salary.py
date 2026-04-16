import pyspark
from pyspark.sql import Window
import pyspark.sql.functions as F

salaryWindow = Window.partitionBy('salary')

output = worker.withColumn('same_salary',
    F.count('worker_id').over(salaryWindow)
).filter(F.col('same_salary') > 1).select(
    'worker_id', 'first_name', 'salary'
).orderBy('salary', descending=True)

output.toPandas()
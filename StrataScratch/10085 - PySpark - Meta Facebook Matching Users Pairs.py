# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = facebook_employees.select(
    F.col('id').alias('id1'),
    F.col('age').alias('second_age'),
    F.col('location').alias('second_location'),
    F.col('gender').alias('second_gender'),
    F.col('is_senior').alias('second_is_senior')
).join(
    facebook_employees.withColumnRenamed('id', 'id2'),
    (F.col('location') == F.col('second_location')) &
    (F.col('age') != F.col('second_age')) &
    (F.col('gender') == F.col('second_gender')) &
    (F.col('is_senior') != F.col('second_is_senior')),
    how = 'cross'
).select('id1', 'id2')

# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()

###############################################################################

# Optimized version:
emp1 = facebook_employees.alias("e1")
emp2 = facebook_employees.alias("e2")

output = (
    emp1.join(
        emp2,
        (
            (F.col("e1.location") == F.col("e2.location")) &
            (F.col("e1.age") != F.col("e2.age")) &
            (F.col("e1.gender") == F.col("e2.gender")) &
            (F.col("e1.is_senior") != F.col("e2.is_senior"))
        )
    )
    .select(
        F.col("e1.id").alias("id1"),
        F.col("e2.id").alias("id2")
    )
)
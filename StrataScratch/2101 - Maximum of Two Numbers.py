import pyspark
import pyspark.sql.functions as F

deloitte_numbers_2 = deloitte_numbers.withColumnRenamed('number', 'number2')
deloitte_numbers = deloitte_numbers.withColumnRenamed('number', 'number1')

output = deloitte_numbers.crossJoin(deloitte_numbers_2).withColumn(
    'max_number',
    F.when(
        F.col('number1') > F.col('number2'),
        F.col('number1')
    ).otherwise(
        F.col('number2')
    )
)

output.toPandas()
##################################################################################

# Optimized solution
df1 = deloitte_numbers.alias('df1')
df2 = deloitte_numbers.alias('df2')

output = df1.crossJoin(df2).select(
    F.col('df1.number').alias('number1'),
    F.col('df2.number').alias('number2'),
    F.greatest(F.col('df1.number'), F.col('df2.number')).alias('max_number')
)

output.toPandas()
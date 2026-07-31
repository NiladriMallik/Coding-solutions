# Import your libraries
import pyspark
from pyspark.sql import functions as F

# Start writing code
output = sf_restaurant_health_violations.withColumn(
    'no_risk_results',
    F.when(F.col('risk_category').isNull(), 1).otherwise(0)
).withColumn(
    'low_risk_results',
    F.when(F.col('risk_category') == 'Low Risk', 1).otherwise(0)
).withColumn(
    'medium_risk_results',
    F.when(F.col('risk_category') == 'Moderate Risk', 1).otherwise(0)
).withColumn(
    'high_risk_results',
    F.when(F.col('risk_category') == 'High Risk', 1).otherwise(0)
).groupBy('inspection_type').agg(
    F.sum('no_risk_results').alias('no_risk_results'),
    F.sum('low_risk_results').alias('low_risk_results'),
    F.sum('medium_risk_results').alias('medium_risk_results'),
    F.sum('high_risk_results').alias('high_risk_results'),
).withColumn(
    'total_inspections',
    F.col('no_risk_results')
    + F.col('low_risk_results')
    + F.col('medium_risk_results')
    + F.col('high_risk_results')
).orderBy(F.desc('total_inspections'))



# To validate your solution, convert your final pySpark df to a pandas df
output.toPandas()
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window as W
import pyspark
import datetime
import json

spark = SparkSession.builder.appName('run-pyspark-code').getOrCreate()

def etl(rp_employees, rp_payroll):
    # Write code here
    return rp_employees.join(
        rp_payroll,
        on = 'employee_id'
    ).withColumn(
        'pay', F.col('hours_worked') * F.col('hourly_rate')
    ).select(
        'employee_id', 'name', 'pay', 'position'
    ).orderBy('employee_id')

    
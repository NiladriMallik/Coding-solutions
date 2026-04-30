from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def etl(bne_countries_val):
    return bne_countries_val.filter(
        (F.col('area') >=3000000) |
        (F.col('population') >= 25000000)
    ).select(
        'name', 'population', 'area'
    )
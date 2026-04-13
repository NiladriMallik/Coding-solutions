import pyspark

output = winemag_p2.filter(
    (winemag_p2['taster_name'] == 'Roger Voss') &
    (winemag_p2['region_1'].isNotNull())
).select('variety').distinct()

output.toPandas()
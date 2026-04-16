import pyspark

output = winemag_p1.select('variety').unionAll(
    winemag_p2.select('variety')
).distinct()

output.toPandas()
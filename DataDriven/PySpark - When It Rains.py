from pyspark.sql import functions as F

result = err_tracks.filter(
    F.when(
        F.col('err_type').like('%Error%'), 1
    ).otherwise(0) +
    F.when(
        F.col('message').like('%null%'), 1
    ).otherwise(0) +
    F.when(
        F.col('svc_name').like('%api%'), 1
    ).otherwise(0) +
    F.when(
        F.lower(F.col('severity')) == 'error', 1
    ).otherwise(0)
    > 1
)

result.show()
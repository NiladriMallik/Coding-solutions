import pyspark
import pyspark.sql.functions as F

output = google_file_store.filter(
    (F.col('contents').contains('optimism')) &
    (F.col('filename').contains('draft'))
)

output.toPandas()
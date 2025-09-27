from pyspark.sql import functions as F

employees_df\
    .filter(
		(F.col('mentor_id') != 3) |
  		(F.col('mentor_id').isNull())
        )\
            .select('name')\
                .show()

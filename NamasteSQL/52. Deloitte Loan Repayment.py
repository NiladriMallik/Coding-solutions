from pyspark.sql import functions as F

#loans_df.show()
#payments_df.show()

joined_df = loans_df.join(
	payments_df,
  	loans_df.loan_id == payments_df.loan_id,
  	how = 'left'
)\
.groupby(loans_df.loan_id)\
.agg(
  	F.max(loans_df.loan_amount).alias('loan_amount'),
	F.max(loans_df.due_date).alias('due_date')
)\
.withColumn('fully_paid_flag',
            when(F.sum(payments_df.amount_paid) == F.max(loans_df.loan_amount), pl.lit(1))\
            .otherwise(pl.lit(0))
)
.select(['loan_id', 'loan_amount', 'due_date'])\
.show()

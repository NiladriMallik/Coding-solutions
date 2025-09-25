from pyspark.sql import functions as F

# product_reviews_df.show(truncate=False)

product_reviews_df.withColumn('lower_review_text', F.lower('review_text'))\
    .filter(
        ((F.col('lower_review_text').contains('excellent')) | (F.col('lower_review_text').contains('amazing')))
        & ~((F.col('lower_review_text').contains('not amazing')) | (F.col('lower_review_text').contains('not excellent')))
        ).select('review_id', 'product_id','review_text')\
            .sort(F.col('review_id').asc())\
                .show(truncate = False)


# Better query

product_reviews_df.withColumn('lower_review_text', F.lower('review_text'))\
    .filter(
        (
            F.col('lower_review_text').like('%excellent%') |
            F.col('lower_review_text').like('%amazing%')
         )&
         ~(
             F.col('lower_review_text').like('%not amazing%') |
             F.col('lower_review_text').like('%not excellent%')
        )
    )\
        .select('review_id', 'product_id','review_text')\
            .sort(F.col('review_id').asc())\
                .show(truncate = False)
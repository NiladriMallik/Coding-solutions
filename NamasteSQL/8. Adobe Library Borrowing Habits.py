from pyspark.sql import functions as F

books_df.join(borrowers_df,
              books_df['BookID'] == borrowers_df['BookID'],
              how = 'RIGHT'
              ).groupBy('BorrowerName')\
                .agg(F.collect_set('BookName')\
                     .alias('BorrowedBooks'))\
                        .withColumn('BorrowedBooks', F.array_sort('BorrowedBooks'))\
                            .withColumn('BorrowedBooks', F.concat_ws(",", "BorrowedBooks"))\
                                .sort(F.col('BorrowerName').asc())\
                                    .show(truncate = False)
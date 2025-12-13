# Polars
import polars as pl
import pandas as pd

# Dataset is loaded as a LazyFrame
lf = ms_user_dimension.head()

# My solution
df1 = ms_user_dimension.join(ms_acc_dimension, on = 'acc_id', how = 'inner').join(
    ms_download_facts,
    on = 'user_id',
    how = 'left'
).select(['paying_customer', 'downloads', 'date'])

df1.filter(
    pl.col('paying_customer') == 'yes'
).group_by('date').agg(
    pl.col('downloads').sum().alias('paying')
).join(
    df1.filter(
        pl.col('paying_customer') == 'no'
    ).group_by('date').agg(
        pl.col('downloads').sum().alias('non_paying')
    ),
    
    on = 'date',
    how = 'inner'
).filter(
    pl.col('non_paying') > pl.col('paying')
).sort('date', descending = False)

##########################################################

# Optimized solution by ChatGPT
df1 = (
    ms_user_dimension
    .join(ms_acc_dimension, on = 'acc_id', how = 'inner')
    .join(ms_download_facts, on = 'user_id', how = 'left')
    .select(['paying_customer', 'downloads', 'date'])
    .group_by('date')
    .agg([
        (
            pl.when(pl.col('paying_customer') == 'yes')
            .then(pl.col('downloads'))
            .otherwise(0)
        ).sum().alias('paying'),
        
        (
            pl.when(pl.col('paying_customer') == 'no')
            .then(pl.col('downloads'))
            .otherwise(0)
        ).sum().alias('non_paying')
    ]).filter(pl.col('paying') < pl.col('non_paying'))
    .sort('date')
)

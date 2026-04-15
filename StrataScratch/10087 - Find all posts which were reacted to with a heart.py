import pyspark
import pyspark.sql.functions as F

output = facebook_posts.join(facebook_reactions,
    on = ['post_id', 'poster'],
    how = 'inner'
).filter(F.col('reaction') == 'heart').select(
    'post_id', 'poster', 'post_text', 'post_keywords', 'post_date'
).distinct()

output.toPandas()
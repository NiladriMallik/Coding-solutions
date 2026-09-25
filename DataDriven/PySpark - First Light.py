from pyspark.sql import functions as F

results = ci_builds.filter(
    F.lower(F.col('status')) == 'success'
).groupBy(
    'repo_name'
).agg(
    F.min('built_at').alias('earliest_build')
).join(
    repo_commits,
    on='repo_name',
    how='inner'
).filter(
    F.col('commit_at') < F.col('earliest_build')
).groupBy(
    'author'
).agg(
    F.avg('added').alias('avg_lines_added'),
    F.avg('removed').alias('avg_lines_removed'),
).orderBy(
    F.col('avg_lines_added').desc(),
    F.col('author').asc()
)

results.show()
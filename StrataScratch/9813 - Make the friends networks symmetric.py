import pyspark

gfn = google_friends_network.selectExpr('friend_id as user_id', 'user_id as friend_id')

output = gfn.union(
    google_friends_network
).dropDuplicates().orderBy("user_id", 'friend_id')

output.toPandas()
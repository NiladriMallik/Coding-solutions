# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking['position'] == 1]\
.groupby('trackname')['position']\
.count()\
.reset_index(name = 'times_top1')\
.sort_values('times_top1', ascending = False)
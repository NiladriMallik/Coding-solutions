# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking\
.groupby('artist')['position']\
.count()\
.reset_index(name = 'n_occurrences')\
.sort_values('n_occurrences', ascending = False)
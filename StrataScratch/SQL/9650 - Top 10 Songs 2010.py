# Import your libraries
import pandas as pd

# Start writing code
billboard_top_100_year_end\
.query("year == 2010")\
.drop_duplicates(subset = 'song_name', keep = 'last')\
.sort_values('year_rank', ascending = True)[['year_rank', 'group_name', 'song_name']]\
.head(10)
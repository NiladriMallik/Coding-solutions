# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014.loc[forbes_global_2010_2014['sector'] == 'Financials'] \
    .sort_values('profits', ascending = False) \
        .head(1)[['company', 'continent']]
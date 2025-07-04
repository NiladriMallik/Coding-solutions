# Import your libraries
import pandas as pd

# Start writing code
titanic.head()
survivor = pd.crosstab(titanic['survived'], titanic['pclass'])
survivor.columns = ['first_class', 'second_class', 'third_class']
survivor.reset_index()
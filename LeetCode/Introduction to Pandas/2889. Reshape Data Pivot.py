import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    result = pd.pivot_table(weather, values = 'temperature', index = 'month', columns = 'city')
    return result
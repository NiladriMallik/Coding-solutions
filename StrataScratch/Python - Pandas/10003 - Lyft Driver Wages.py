# Import your libraries
import pandas as pd

# Start writing code
lyft_drivers[(lyft_drivers['yearly_salary'] <= 30000) | (lyft_drivers['yearly_salary'] >= 70000)]
# Import your libraries
import pandas as pd

# Start writing code
employee.sort_values('salary', ascending = False).head(2).tail(1)[['salary']]

# ChatGPT way
second_highest = employee[['salary']].nlargest(2, 'salary').tail(1)
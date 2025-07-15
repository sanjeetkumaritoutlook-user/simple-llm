import pandas as pd
import os
print("Current directory:", os.getcwd())
df = pd.read_csv('data.csv')
print(df.head())          # View first 5 rows
print(df['age'].mean())   # Mean of 'age' column

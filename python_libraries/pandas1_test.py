import pandas as pd
import os

print("Current directory:", os.getcwd())

df = pd.read_csv('data1.csv', delimiter=',')  # Explicit delimiter
print(df.head())
print(df['age'].mean())

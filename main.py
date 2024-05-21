import pandas as pd

df = pd.read_csv('US_PopTotal_20230713030810.csv')
print(df.head( ))

df.info()
print(df.describe())
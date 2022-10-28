
import pandas as pd 

df = pd.read_csv('input/Sodium_data.csv')

df.to_parquet('outpot/Sodium_data.parquet')

print(df)
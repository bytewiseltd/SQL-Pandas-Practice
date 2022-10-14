import pandas as pd


df = pd.read_json ('Input/Sample_Json.json')

df.to_csv ('Output/Sample_JSON-CSV.csv', index = None)

# print  (df)
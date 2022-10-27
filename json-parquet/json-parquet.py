import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq


#conda install pandas
#conda install pyarrow


data = pd.read_json('Input/input.json')
data.to_parquet('Output/output.json')
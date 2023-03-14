import pandas as pd
import numpy as np

data = pd.read_csv('data/descompress/resident-population/ethnical.csv',sep='|',  index_col=0)

df = data['year']
#df = data[(data['year'] >= 2000) & (data['year'] <= 2015)]
#df_save = df.to_csv('processed/ethnical_2000_2015.csv', sep = '|', index=False)
print(df.head(10))
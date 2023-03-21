import pandas as pd


data = pd.read_csv('data/descompress/resident-population/ethnical.csv', names=['year', 'ethnic', 'olds', 'value'] , delimiter ='|' , header = 1)

df = [data['year'].astype(int)>2000]

print(df.head())
#('data/renamed_data/2000_years.csv', sep = '\t' , index = False, na_rep ='N/A')




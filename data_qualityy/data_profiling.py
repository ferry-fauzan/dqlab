import pandas as pd
import numpy as np
import io
# import pandas_profiling
raw=pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv')

print(raw.head())
# cara mencari tau panjang include #n/a
length_city=len(raw["city"])
print("Length City: ", length_city)

#cara mencari tau kolom tanpa #n/a
count_city=raw["city"].count()
print("Count City: ", count_city)

number_miss_value=length_city-count_city
ratio_miss_value=(number_miss_value/length_city)
pct_of_missing_values='{0:.1f}%'.format(ratio_miss_value * 100)
print("Ration miss values", pct_of_missing_values)

#max and min
print('Item Price Min',int(raw['item_price'].min()))
print('Item Price Max',int(raw['item_price'].max()))
print('Item Price Median',int(raw['item_price'].median()))
print('Item Price Mean', int(raw['item_price'].mean()))
print('Item Price Standard Deviasi', int(raw['item_price'].std()))

#mencari quantile
print("Nilai Quratil dari Item Price:") 
print(raw['item_price'].quantile([.25,.5,.75]))

#Correlation
print("Korelasi antara item price dan quantity: ")
print(raw[['quantity','item_price']].corr())
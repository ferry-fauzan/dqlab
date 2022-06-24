import pandas as pd
raw= pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

print(raw['Produk'].head())

data_dummy=pd.get_dummies(raw['Produk'])
print(data_dummy)
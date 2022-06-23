import numpy as np
import pandas as pd
raw= pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

print(raw.head())
#cara filter pada sebuah kolom
produk_A=raw[raw['Produk']=='A']
print(produk_A.head())

#mencari mean
print("Mean:", int(produk_A['Pendapatan'].mean()))
print("Mean:", np.mean(produk_A['Pendapatan']))

#mencari median
print("Median:", raw['Pendapatan'].median())
print("Median:", np.median(raw['Pendapatan']))

#mencari modus/value counts
print("Value Counts/Modus:\n", raw['Produk'].value_counts())

#mencari quantile
print("Quantile:", raw['Pendapatan'].quantile(q=0.25))
print("Quantile:", np.quantile(raw['Pendapatan'], q=0.5))

#menghitung beberapa kolom sekaligus dengan agg()
print("Agg beberapa kolom:\n",raw[['Pendapatan','Harga','Produk','Total']].groupby('Produk').agg([np.mean, np.median]))

#proporsi sebaran dari sebuah data
print("Proporsi:\n", raw['Produk'].value_counts()/raw.shape[0])

#mengetahui variasi
print("Variansi Data:", raw['Pendapatan'].var(ddof=0))

#standard deviasi
print("Standard Deviasi: ", raw['Pendapatan'].std())

#Korelasi
print("Korelasi Pearsonn:\n", raw.corr())
print("Korelasi Kendall:\n",raw.corr(method="kendall"))
print("Korelasi Spearman:\n",raw.corr(method='spearman'))
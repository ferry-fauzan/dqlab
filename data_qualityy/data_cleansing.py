import pandas as pd
import numpy as np
import io
raw=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced_data_quality.csv")

#cek kolom yang memiliki missing value
print("Cek missing Values")
print(raw.isnull().any())

#filling missiing values
print("Mengisi missing value dengan nilai tengah")
print(raw["quantity"].fillna(raw.quantity.mean()))

#drop missing values
print("Menghapus missing values")
print(raw["quantity"].dropna().head())
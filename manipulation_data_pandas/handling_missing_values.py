import pandas as pd

data=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/datacovid19.csv")
#cek indo
print(data.info())
#cek miss value dengan isna()=mngetahui berapa missing value
print("Missing Value per kolom: ")
print(data.isna().sum())


#handling missing values dengan dropna
print("Data awal:", data.shape)
#menghapus kolom (1) dengan missing values semua
data_drop=data.dropna(axis=1,how="all")
print("Setelah dihapus kolom:", data_drop.shape)

#menghapus 
data_dropp=data.dropna(axis=0, how="any")
print("Setelah dihapus baris missing: ", data_dropp.shape)


#handling missing value dengan mengganti string
print("Data sebelum handling: ", data["province_state"].unique())
data["province_state"]=data["province_state"].fillna("ga tau kok nanya saya")
print("Data setelah handling: ", data["province_state"].unique())


#handling value dengan statistika median mean
print(data["fips"].isna().sum())
print(data["fips"])
data["fips"]=data["fips"].fillna(data["fips"].mean())
print(data["fips"].isna().sum())
print(data["fips"])
print(data)
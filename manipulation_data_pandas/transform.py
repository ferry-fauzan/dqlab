import pandas as pd
data=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")

#transformasi order_date ke data date
data["order_date"]=pd.to_datetime(data["order_date"])
print(data.dtypes)

print("Data Baru: ", data.dtypes)

#trransform int ke float
data["quantity"]=pd.to_numeric(data["quantity"],downcast="float")
#transform object ke category
data["city"]=data["city"].astype("category")

print("Data Baru: ", data.dtypes)

#menggunakan map dan apply dengan lambda
print("data awal\n", data.head())
#map
data_map=data["brand"].map(lambda x: x.lower())
print(data_map.head())
#apply
data_apply=data["brand"].apply(lambda x: x[-1].upper())
print(data_apply.head())


#menggunakan fungsi dengan apply map
raw_data=pd.DataFrame([[1,2,3,],
            [2,3,4],
            [3,4,5]])
def quadratic(x):
    return x**2+5*2

raw_data_tf=raw_data.applymap(quadratic)
print("Applymap dengan fungsi:\n ", raw_data_tf)
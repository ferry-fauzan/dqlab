import pandas as pd
df=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")

df_slice=df.loc[(df["brand"]=="BRAND_C") &
                (df["customer_id"].isin(["17091","18055"]))]
                #(df["customer_id"==18055])]

print(df_slice)
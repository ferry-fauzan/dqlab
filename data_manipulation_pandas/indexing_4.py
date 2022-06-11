import pandas as pd
df=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv",sep="\t")

# print("Data frame awal", df)

print(f'index: {df.index}')
# print(f'column: {df.columns}')

df.index=["Pesanan nomor: " + str (i) for i in range(1,102)]
print("Ini yang baru: " ,df)
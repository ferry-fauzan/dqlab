import pandas as pd

# cara 1_menggunkan .index
raw_data=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv",sep="\t", nrows=10)

print("Data awal: ", raw_data)
#pengulangan data index
raw_data.index=["Pesanan ke: "+ str(i) for i in range(1,12)]
print("Data Baru: ", raw_data)


#cara 2 langsung pada read_csv
raw_data=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv",sep="\t", index_col=['order_id'])

print(raw_data)

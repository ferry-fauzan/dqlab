import pandas as pd
# Baca file TSV sample_tsv.tsv
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t", index_col=["order_date"])

print("Index berdasarkan column: ", df.head(4))

# import pandas as pd
# # Baca file sample_tsv.tsv dan set lah index_col sesuai instruksi
# df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv",sep="\t", index_col=["order_date"])
# # Cetak data frame untuk 8 data teratas
# print("Dataframe:\n", df)
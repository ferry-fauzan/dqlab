import pandas as pd

order=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")


sort_harga=order.sort_values(by="product_weight_gram",ascending=0)

print(sort_harga)


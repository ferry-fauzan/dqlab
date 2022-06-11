import pandas as pd

oder=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

q1=oder[["product_weight_gram"]].quantile(0.25)
q3=oder[["product_weight_gram"]].quantile(0.75)

IQR=q3-q1

print(IQR)
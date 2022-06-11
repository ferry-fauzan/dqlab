from turtle import pd
import pandas as pd

order=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

order.rename(columns={"freight_value":"shipping_cost"},inplace=True)

print(order)
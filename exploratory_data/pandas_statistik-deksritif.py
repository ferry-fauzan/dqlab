import pandas as pd

data=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

print(data.describe())

print(data.loc[:,"price"].median())
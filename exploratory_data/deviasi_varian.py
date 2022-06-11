import pandas as pd

data=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")


print(data)
#deviasi
print(data.loc[:, "product_weight_gram"].std())

#deviasi
print(data.loc[:,"product_weight_gram"].var())
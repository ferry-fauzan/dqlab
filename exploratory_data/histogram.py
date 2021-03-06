from msilib.schema import ODBCAttribute
import pandas as pd
import matplotlib.pyplot as plt
order_df=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

order_df[["price"]].hist(
    figsize=(4,5),
    bins=10,
    xlabelsize=8,ylabelsize=8
)

plt.show()
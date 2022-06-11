import pandas as pd

order=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

rata_rata=order["price"].groupby(int[order["payment_type"]]).mean()

# print(order)
print(rata_rata)
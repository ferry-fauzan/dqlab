
import pandas as pd
import datetime
import matplotlib.pyplot as plt


#raw data
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
#print(dataset.head(),'\n')



#tambah kolom order month
dataset['order_month']=dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
dataset['GMV']=dataset['item_price']*dataset['quantity']

print(dataset.head())
plt.figure(figsize=(10,5))
dataset[dataset['order_month']=='2019-12'].groupby(['order_date'])['customer_id'].nunique().plot(color='green',marker='.',linewidth=2)
plt.xlabel('Order Date')
plt.ylabel('Count of Customer ID')
plt.grid(color='darkblue',linestyle='-.',linewidth=0.5)
plt.title('DAILY NUMBER CUSTOMER ORDER', loc='center',pad=20, fontsize=20, color='Blue')
plt.ylim(ymin=15)

plt.savefig('Customer ID', quality=95)
plt.show()
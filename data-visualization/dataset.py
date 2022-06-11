from matplotlib import transforms
from matplotlib.figure import Figure
import pandas as pd
import datetime
import matplotlib.pyplot as plt


#raw data
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
#print(dataset.head(),'\n')

#tambah kolom order month
dataset['order_month']=dataset['order_date'].apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
#print(dataset.head(),'\n')

#tambah kolom GMV
dataset['GMV']=dataset['item_price']*dataset['quantity']
#print(dataset.head(),'\n')

#group order month dengan GMV
monthly_amount=dataset.groupby('order_month')['GMV'].sum().reset_index()
print(monthly_amount)

# #set figure size
plt.figure(figsize=(10,5))
plt.title('GMV THIS YEAR 2019',loc='left', pad=20, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('GMV', fontsize=20)
# dataset.groupby(['order_month'])['GMV'].plot()
# plt.show()

# #membuat line chart dengan menambah variabel baru
# # plt.plot(monthly_amount['order_month'],monthly_amount['GMV'])
# # plt.show()

#dengan dataset python dan edit style
dataset.groupby(['order_month'])['GMV'].sum().plot(color='blue',marker='+',linestyle='-.',linewidth=2)
#setting grid
plt.grid(color='darkblue',linestyle='-',linewidth=0.5)
#menentukan batas min maks y axis
plt.ylim(ymin=0)
#setting plt.yticks
labels,locations=plt.yticks()
plt.yticks(labels,(labels/1000000000).astype(int))
#beriinformasi pada plot
# plt.text(0.45,0.72,'The GMV increased significanly on October 2019',transforms=fig.transfigure,color='red')
# plt.text(0.45,0.72,'The GMV increased significanly on October 2019',color='red')
#cara save gambar
plt.savefig('monthly_gmv.png',quality=95)
plt.show()



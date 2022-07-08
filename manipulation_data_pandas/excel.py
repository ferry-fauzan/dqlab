import pandas as pd

data_excel=pd.read_excel('excels.xlsx',sheet_name='Sheet1')

print('Index: ', data_excel.index)
print('Column', data_excel.columns)

datas=data_excel.set_index(['Kota'])
print(data_excel)
print(datas)

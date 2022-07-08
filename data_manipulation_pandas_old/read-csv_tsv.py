import pandas as pd

#csv dan tsv
csvv=pd.read_csv('https://storage.googleapis.com/dqlab-dataset/sample_csv.csv')
print(csvv.head(2),'\n')

tsvv=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv",sep='\t')
print(tsvv.head(2),'\n')

#excel
excell=pd.read_excel("https://storage.googleapis.com/dqlab-dataset/sample_excel.xlsx",sheet_name="test")
print(excell.head(2),'\n')

#json
url="https://storage.googleapis.com/dqlab-dataset/covid2019-api-herokuapp-v2.json"
jsonn=pd.read_json(url)
print(jsonn.head(2),'\n')
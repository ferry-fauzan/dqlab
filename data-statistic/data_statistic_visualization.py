import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# plt.clf()

raw = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')
#melihat data
print(raw.head())

plt.figure()

#visualisasi diagram pencar
plt.scatter(x='Pendapatan',y='Total',data=raw)
plt.title('Plot Scatter Panda', size=12)
plt.xlabel('Total')
plt.ylabel('Pendapaatan')
plt.tight_layout()

plt.show()

#visualisasi dengan hsitogram
raw.hist(column='Pendapatan')
plt.ylabel=('Pendapatan')
plt.title('Visualisasi dengan Histogram')
plt.tight_layout()
plt.show()


#visualisasi dengam boxplot
raw.boxplot(column='Pendapatan')
plt.title('Visualisasi dengan boxplot')
plt.tight_layout()
plt.show()


#visualisasi dengan barplot
freq=raw['Produk'].value_counts()
print(freq)
freq.plot.bar()
plt.title('Visualisasi dengan barplot')
plt.tight_layout()
plt.show()

#visualisasi dengan pieplot
freq.plot.pie()
plt.title('Visualisasi dengan pie chart')
plt.tight_layout()
plt.show()
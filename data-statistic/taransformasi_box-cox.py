import statistics
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
raw = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

hasil,_=stats.boxcox(raw['Pendapatan'])

#Histogram Pendapatan sebelum transformasi
plt.hist(x='Pendapatan', data=raw)
plt.title('Boxcox Histogram')
plt.tight_layout()
plt.show()

#Histogram Pendapatan Transformasi Boxcox
plt.hist(hasil)
plt.title('Boxcox Histogram')
plt.tight_layout()
plt.show()

#QQPLOT sebelum transformasi
stats.probplot(raw['Pendapatan'],plot=plt)
plt.title('qqplot Sebelum Transformasi', size=14)
plt.tight_layout()
plt.show()

#QQPLOT setealah transformasi
stats.probplot(hasil,plot=plt)
plt.title('qqplot setelah Transformasi', size=14)
plt.tight_layout()
plt.show()
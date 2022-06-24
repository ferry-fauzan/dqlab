from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
raw = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

raw.hist()
plt.title('Histogram Raw Data')
plt.tight_layout()
plt.show()

raw['Pendapatan'].hist()
plt.title('Histogram Pendapatan')
plt.show()

#transformasi menggunakan akar 5
np.power(raw['Pendapatan'],1/5).hist()
plt.title('Hist Pendapatan Menggunakan akar 5')
plt.tight_layout()
plt.show()

pendapatan_akar_5=np.power(raw['Pendapatan'], 1/5)
# print(list(pendapatan_akar_5 , raw['Pendapatan']))

#qqplot dengan raw pendapatan
stats.probplot(raw['Pendapatan'],plot=plt)
plt.title('QQPLOT Pendapatan')
plt.tight_layout()
plt.show()

#qqplot setelah akar 5 transformasi
stats.probplot(pendapatan_akar_5,plot=plt)
plt.title('QQPLOT Transformasi Akar 5')
plt.tight_layout()
plt.show()
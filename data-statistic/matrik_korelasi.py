import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
raw= pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

#data korelasi dengan matplotlib
plt.matshow(raw.corr())
plt.title('Plot correlation matriks dengan .matshow', size=14)
plt.tight_layout()
plt.show()


sns.heatmap(raw.corr(), annot=True)
plt.title('Plot correlation matriks dengan sns.heatmap', size=14)
plt.tight_layout()
plt.show()
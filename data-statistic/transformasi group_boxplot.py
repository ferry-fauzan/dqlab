import pandas as pd
import matplotlib.pyplot as plt
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')


#boxplot dengan all kategori
raw_data.boxplot()
plt.title('Boxplot tanpa pengelompokkan', size=14)
plt.tight_layout()
plt.show()

#boxplot dengan kategori tertentu
raw_data.boxplot(by='Produk')
plt.title('Boxplot dengan pengelompokkan', size=14)
plt.tight_layout()
plt.show()

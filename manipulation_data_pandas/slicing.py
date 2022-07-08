from operator import index
import pandas as pd

raw_data=pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_csv.csv")
#slicing index dengan loc
slicing=raw_data.loc[
                    (raw_data["city"]=="Makassar") &
                    (raw_data["product_id"].isin(["P3388","P3082","P3354","P3357"]))
                    ]
#melakukakn indexing dengan set_index
index=slicing.set_index("Pesanan ke: "+str(i) for i in range(1, 5))
print("Hasil Slicing: ", index)


#cara ke-2 set index dahulu lalu menggunakan fungsi slicing
raw_data1=raw_data.set_index(["order_id", "order_date"])
raw_data1_slicing=raw_data1.loc[([1612339,1612390],"2019-01-01"),:]
print(raw_data1_slicing)
data11 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]

def hitung_rata(data1):
    jumlah1=0
    jumlah2=0

    for rata1 in data1:
        jumlah1=jumlah1+rata1

    # for rata2 in data2:
    #     jumlah2=jumlah2+rata1

    rerata1=jumlah1/len(data1)
    print(rerata1)
    

hitung_rata(data11)
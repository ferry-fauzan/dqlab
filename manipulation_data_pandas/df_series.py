import pandas as pd

number_list=pd.Series([5,1,2,3,4,4,5])
print("Series: ")
print(number_list)
print("Kolom dan Baris:", number_list.shape, "\nTipe Data: ", number_list.dtypes,
        "\nIndex: ", number_list.index)
print("Konversi menjadi list: ", number_list.to_list(), number_list.dtypes)
print("List: ", number_list.unique())
print("loc 1: ", number_list.loc[0:1])
print("loc 2: ", number_list.loc[0:2])
print("iloc 1: ", number_list.iloc[0:1])
print("iloc 2: ", number_list.iloc[0:2])

matrix=pd.DataFrame([[1,2,3],
        ["ani","toni",7],
        ["surau",7,"mushola"],
        [3,5,9]])
# matrix_list=pd.DataFrame(matrix)
print("Dataframe: ")
print(matrix)
print("Kolom dan Baris: ",matrix.shape, "\nTipe Data: ", matrix.dtypes,
        "\nIndex: ", matrix.index, "\nColumns: ", matrix.columns)
print("loc 1: ", matrix.loc[0:1])
print("loc 2: ", matrix.loc[0:2])
print("iloc 1: ", matrix.iloc[0:1])
print("iloc 2: ", matrix.iloc[0:2])


matrixx=[[1,2,3],
        ["ani","toni",7],
        ["surau",7,"mushola"],
        [3,5,9]]
index=['bar1','bar2','bar3','bar4']
kol=['kol1','kol2','kol3']
kol_bar=pd.DataFrame(matrixx,index=index,columns=kol)
print(kol_bar)
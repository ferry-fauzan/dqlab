import pandas as pd

numberList=pd.Series([1,2,3,4,5])
# print('Series')
# print(numberList)

matrix=[[1,2,3],
        ['a','a','f'],
        [1,2,'fg','6d']]
matrixList=pd.DataFrame(matrix)
# print('Data Frame')
# print(matrixList)

print("Att info()")
print("matrixList", matrixList.info())

print("Shape dari Matrixlist", matrixList.shape)
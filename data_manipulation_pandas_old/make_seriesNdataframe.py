import pandas as pd
import numpy as np


#list
list=['andi',24,"front end"]
seriess=pd.Series(list)
print(seriess,'\n')

list_arrayy=[['ojan',25,'front end'],
        ['reska',28,'data sains']]
index=['man1','man2']
columns=['name','age','jobs']
dafaram=pd.DataFrame(list_arrayy,index=index,columns=columns)
print(dafaram,'\n')

#dataframe

dict={'nama':'ojan',
      'jobs':'programmer',
      'age':24  }
seriesss=pd.Series(dict)
print(seriesss,'\n')

dictt={'nama':['ojan','reska','ujik'],
        'jobs':['programmer','influencer','analyst']}
daframmm=pd.DataFrame(dictt)
print(daframmm,'\n')

#numpyarray

arrSeries=np.array([1,2,3,4,5,6])
exSeries=pd.Series(arrSeries)
print(exSeries,'\n')

arrDf=np.array([[1,2,3],
                ['a','b','c']])
exDf=pd.DataFrame(arrDf)
print(exDf)
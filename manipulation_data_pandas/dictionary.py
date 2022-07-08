import pandas as pd
import numpy as np

dictio={'PRO': [22,34,66],
            'ROS': ['AB','GW','GG'],
            '112': [24,'GD',35]}

dict_ke_df=pd.DataFrame(dictio)
print(dict_ke_df)

array_series=np.array([1,2,3,6,7,8])
ubah_np=pd.Series(array_series)
print(ubah_np)

array_df=np.array([[1,5,3,4],
                        ['paijo','bambang','juwari','janji']])
ubah_np2=pd.DataFrame(array_df)
print(ubah_np2)
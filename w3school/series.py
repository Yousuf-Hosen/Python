import pandas as pd
a=[3,7,6,5,4,2]
# val=pd.Series(a)
# print(val)
# # we can level it default level start with 0
# print(val[1])
# print(val[2])
# print(val[3])
#  customizelevel by decide
val=pd.Series(a,index=["First",2,3,4,5,6])
print(val["First"])
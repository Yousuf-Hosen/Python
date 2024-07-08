import pandas as pd
calories={"Day1":420, "Day2":230, "Day3":330}
# print all elements present in series 
# res=pd.Series(calories)
# print(res)
# but we can access difinite number elememnts
val=pd.Series(calories,index=["Day1","Day3"])
print(val)
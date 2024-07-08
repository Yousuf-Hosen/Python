import math
def exp(a,x):
    res=pow(a,x)
    return res
x, y = map(int, input().split())
output=exp(x,y)
print("result is : ",output)
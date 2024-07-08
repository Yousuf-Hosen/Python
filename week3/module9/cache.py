import time
from functools import cache
@cache
def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)
start=time.time()
for i in range(30):
    print(i,fib(i))
end=time.time()
mili_seconds=(end-start)*1000
print('time take ->',mili_seconds)
# without cache 
# time take -> 1999.6371269226074

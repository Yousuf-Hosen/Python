import math
import time
def timer(fun):
    def innner(*args,**kwargs):
        start=time.time()
        print(start)
        fun(*args,**kwargs)
        time_end=time.time()
        print(time_end)
        print(f'the total times needs for op is ->{time_end-start}')
    return innner
@timer # this is called decoration
def get_factorial(n):
    result=math.factorial(n)
    print(f'factorial of {n} is {result}')
# timer(get_factorial)()
get_factorial(n=112)

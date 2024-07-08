# def Do_something(x,y):
#     print(f'x:{x} and y:{y}')
# Do_something(12,77)
# Do_something('tomato','alu')
""" 
we can send a function as a parameters in  python code

 """
def do_something(work):
    # print(work) # that received a python function that can not exact the function attributes
    work() # we call the function that weorking 

def practing_code():
    print('i am practing python codeing')
# do_something(practing_code)

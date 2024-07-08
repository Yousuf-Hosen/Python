def do_something():
    print('inside the do something function')
    def inner_functiuon():
        print('inside the inner function')
    inner_functiuon() #  call the inner function
# do_something()

def first_function():
    print('inside the first function')
    def second_function():
        print('inside the 2nd function')
    return second_function # this is return but if we use () then it is done call



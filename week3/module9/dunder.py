class Person:
    def __init__(self,name,age,money):
        self.name=name
        self.age=age
        self.money=money
    def __add__(self,other): # this is special method
        return self.money+other.money
    def __sub__(self,other):
        return self.money-other.money
    def __call__(self):
       print(f'this is an object of {self.name} ,his age is {self.age} and he have {self.money} taka')

person_1=Person("abul",23,4000)
person_2=Person("kabul",21,5000)
# print(person_1+person_2)
# print(person_1-person_2)
# person_1() # person object not callable
person_2()

#method overloading
def add(num1,num2,num3=0):
    return num1+num2+num3

# result=add(21,12)
# print(result)
# print(add(12,13))
# print(add(12,13,15))


#operator overloading

# print(12+34)
# print("H"+" W")



# class Account:
#     def __init__(self,Holder,balance):
#         self.Holder=Holder
#         self.__balancce=balance


#     def __add__(self,other):
#         return self.__balance+other.__balance


# my_account=Account('shakib',60000)
# her_account=Account("Shisir vabi",7990000)
# result=add()
# print(result)




class A:
    def __init__(self) -> None:
        self.multiply(15)
        print(self.i)
    def multiply(self,i):
        self.i=4*i
class B(A):
    def __init__(self) -> None:
        super().__init__()
    def multiply(self, i):
        self.i=2*i
obj=B()
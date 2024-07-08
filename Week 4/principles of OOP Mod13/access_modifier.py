#public
#protected
#private
class account:
    def __init__(self,holder,school) -> None:
        self.account_holder=holder
        self.school=school

  
class student_account(account):
    def __init__(self,holder,balance,school):
        super().__init__(holder,school)
        self.__balance=balance
    def withdraw(self,amount):
        if amount>self.__balance:
            return 'There is no money for you'
        self.__balance-=amount
        return f'withdrawn amount {amount}'
    

    
    def deposit(self,amount):
        if amount<0:
            return 'Negative amount can not be deposited'
        self.__balance+=amount
    def get_balance(self):
        return self.__balance


yousuf=student_account("Yousuf",2500,"MEC")
# yousuf.__balance=899888
yousuf.deposit(50000)
yousuf.withdraw(30000)
print(yousuf.get_balance())
# print(dir(yousuf))
print(yousuf._student_account__balance)
class Account:
    def __init__(self,holder,initial_balance):
        self.holder=holder # public attribute
        self._account_number=169 # convention/protection
        self.__balance=initial_balance # private attribute
    
    def deposit(self,amount):
        print(f'deposit money {amount} in yourt account')
        self.__balance+=amount
    

    def Withdraw(self,amount):
        print(f'withdrawing money {amount} from your account')
        self.__balance-=amount




class Student_account(Account):
    def __init__(self,holder,initial_balance,school):
        self.school=school
        super().__init__(holder,initial_balance)
    
    def get_balance(self):
        return self._account_number
    

raju=Student_account("Raju ahmed",5000,"PKHS")
# print(raju.__balance)
raju.deposit(30000)
raju.Withdraw(10000)
# raju.__balance=0
print(raju.get_balance())
print(raju._account_number)
print(raju._Account__balance)

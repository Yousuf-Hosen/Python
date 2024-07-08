""" Manage bank account """

class Account:
    AC_id=1
    def __init__(self,name,age,nid_num,balance):
        self.name=name
        self.age=age
        self.nid_num=nid_num
        self.balance=balance

        #update account id
        self.Account_id=Account.AC_id # class er name diye increase korte hobe
        Account.AC_id+=1
    
# Deposit function
    def Deposit(self,amount):
        if self.balance>0:
           self.balance+=amount
           print(f'your {amount} taka Deposit successfully')

        else:
            print("You entered error amount")


    
#withdraw function
    def Withdraw(self,amount):
        if self.balance>amount:
           self.balance-=amount
           print(f'your {amount} taka withdraw successfully')

        else:
            print("You entered error amount")
    def Delete_account(self,account_id,name,nid_num):
        if self.Account_id==account_id & self.name==name & self.nid_num==nid_num:
            print(f'Your account number {account_id} , {name} and {nid_num} is matched ')
            



acc1=Account("Munna",32,1344234,6000)
# print(acc1.balance)
# print(acc1.Account_id)

acc2=Account("Munna vaii",42,135324234,600)
print(acc2.Account_id)
acc1.Deposit(2000)
print("Balance of account1 ->",acc1.balance)
acc1.Withdraw(3000)
print("Balance of account1 ->",acc1.balance)


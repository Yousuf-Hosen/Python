class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=10000
    def get_balance(self):
        return self.balance
    def withdraw(self,amount):
        if amount<self.min_withdraw:
            return f'you have no balance for  withdraw . minimum withdraw ->{self.min_withdraw}'
        elif amount>self.max_withdraw:
            return f'You croseed your daily limit :{self.max_withdraw}'
        elif amount>self.balance:
            return f'you have no money, you have ->{self.balance} taka now'
        else:
            self.balance=self.balance-amount
            return f'here is your money -> {amount}'
    def diposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
my_bank=Bank(8000)
reply=my_bank.withdraw(2000)
print(reply)
print(my_bank.get_balance())
reply=my_bank.withdraw(3000)
print(reply)
print(my_bank.get_balance())
add_money=my_bank.diposit(10000)
print(my_bank.get_balance())
reply=my_bank.withdraw(5000)
print(reply)
print(my_bank.get_balance())



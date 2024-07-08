import hashlib
from random import random,randint
from BRTA import Brta
from vehicles import Car
from vehicles import Bike
from vehicles import Cng
from ride_manager import uber
class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.save_user=[]
        pass_encryted=hashlib.md5(password.encode()).hexdigest()
        with open("user.text","w") as file:
            
            x=file.write(f'{email} {pass_encryted}')
            self.save_user.append(x)
        file.close()
        print(f'{self.name} user created ')
    @staticmethod
    def Log_in(self,email,password):
        stored_password=" "
        with open("user.text","r") as file:
            # lines=file.readlines()
            # for line in lines:
            #     if email in line:
            #         # print(line)
            #         stored_password=line.split(' ')[1]    
            for line in self.save_user: 
                if email in line:
                    stored_password=line.split()[1]
        file.close()

        hash_password=hashlib.md5(password.encode()).hexdigest()
        if stored_password==hash_password:
            print("Valid user")
            return True
        else:
            print("Password not matched, invalid user")
            return False
        # print('Password found ',stored_password)

    
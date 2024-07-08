import hashlib
from random import random,randint
from BRTA import Brta
from vehicles import Car
from vehicles import Bike
from vehicles import Cng
from ride_manager import uber

license_authority=Brta()
class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        pass_encryted=hashlib.md5(password.encode()).hexdigest()
        with open("user.text","a") as file:
           file.write(f'{email} {pass_encryted} \n')           
        file.close()
        print(f'{self.name} user created ')
    @staticmethod
    def Log_in(self,email,password):
        stored_password=" "
        with open("user.text","r") as file:
            lines=file.readlines()
            for line in lines:
                if email in line:
                    stored_password=line.split(' ')[1]    
        file.close()

        hash_password=hashlib.md5(password.encode()).hexdigest()
        if stored_password==hash_password:
            print("Valid user")
            return True
        else:
            print("Password not matched, invalid user")
            return False
        # print('Password found ',stored_password)


class Rider(User):
    def __init__(self, name, email, password,Location,Balance):
        self.Location=Location
        self.Balance=Balance
        super().__init__(name, email, password)
    def Set_Location(self,location):
        self.Location=location
    def Get_Location(self):
        return self.Location
    def Request_Trip(self,Start,Destination):
        pass
    def Start_a_Trip(self,fare):
        self.Balance-=fare

class Driver(User):
    def __init__(self, name, email, password,Location,License,phone):
        super().__init__(name, email, password)
        self.Location=Location
        self.License=License
        self.phone=phone
        self.valid_driver=license_authority.Check_license(email,License)
        self.earning=0
    def take_driving_test(self):
        result=license_authority.Take_Driving_test(self.email)
        if result==False: 
            print("sorry You failed, try again")
        else:
            self.License=result
            self.valid_driver=True
    
    def register_a_vehicle(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            new_vehicle=None
            if vehicle_type=='car':
                new_vehicle=Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,new_vehicle)
                print(f'vehicle {vehicle_type} is registered')
            elif vehicle_type=='bike':
                new_vehicle=Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,new_vehicle)
                print(f'vehicle {vehicle_type} is registered')
            else:
                new_vehicle=Cng(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,new_vehicle)
                print(f'vehicle {vehicle_type} is registered')


        else:
            print("You are not a valid driver")

    def start_a_trip(self,destination,fare):
        self.earning+=fare
        self.Location=destination
        

rider1=Rider('rider1','rider1@gmail.com','rider1sr',randint(0,30),5000)

rider2=Rider('rider2','rider2@gmail.com','rider2sr',randint(0,30),7500)
# print(dir(rider2))

driver1=Driver('driver1','driver1@gmail.com','driver1',randint(0,30),10022,'0172571357')
driver1.take_driving_test()
driver1.register_a_vehicle('car',12345,15)
driver2=Driver('driver2','driver2@gmail.com','driver2',randint(0,30),10055,'01725713754') 
driver2.take_driving_test()
driver2.register_a_vehicle('bike',12398,25)
driver3=Driver('driver3','driver3@gmail.com','driver3',randint(0,30),10034,'01725713575')
driver3.take_driving_test()
driver3.register_a_vehicle('car',12398,15)
driver4=Driver('driver4','driver4@gmail.com','driver4',randint(0,30),10078,'01725713572')
driver4.take_driving_test()
driver4.register_a_vehicle('car',4554,10)

print(uber.get_available_cars())

uber.find_a_vehicle(rider1,'car',90)



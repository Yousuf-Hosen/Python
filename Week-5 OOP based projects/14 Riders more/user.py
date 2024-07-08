import hashlib
from random import random,randint,choice
import threading
from BRTA import Brta
from vehicles import Car
from vehicles import Bike
from vehicles import Cng
from ride_manager import uber 
from plyer import notification


class UserAlreadyExist(Exception):
    def __init__(self,email, *args: object) -> None:
        print(f"User {email} already exists")
        super().__init__(*args)

license_authority=Brta()
class User:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        pass_encryted=hashlib.md5(password.encode()).hexdigest()
        already_exists=False
        with open('user.txt','r') as file:
            if  email in file.read():
                already_exists=True
                # raise UserAlreadyExist(email)
        file.close()


        
        if already_exists==False:
            with open("user.txt","a") as file:

                file.write(f'{email} {pass_encryted} \n')           
            file.close()
        # print(f'{self.name} user created ')

    @staticmethod
    def Log_in(self,email,password):
        stored_password=" "
        with open("user.txt","r") as file:
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
        self.__trip_history=[]
        self.Balance=Balance
        super().__init__(name, email, password)
    def Set_Location(self,location):
        self.Location=location
    def Get_Location(self):
        return self.Location
    def Request_Trip(self,Start,Destination):
        pass
    
    def get_trip_history(self):
        return self.__trip_history
    def Start_a_Trip(self,fare,trip_info):
        print(f'a trip is started for {self.name}')
        self.Balance-=fare
        self.__trip_history.append(trip_info)


class Driver(User):
    def __init__(self, name, email, password,Location,License,phone):
        super().__init__(name, email, password)
        self.Location=Location
        self.__trip_history=[]
        self.License=License
        self.phone=phone
        self.valid_driver=license_authority.Check_license(email,License)
        self.earning=0
        self.vehicle=None

    def take_driving_test(self):
        result=license_authority.Take_Driving_test(self.email)
        if result==False: 
            # print("sorry You failed, try again")
            self.License=None
        else:
            self.License=result
            self.valid_driver=True
    
    def register_a_vehicle(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            self.vehicle=None
            if vehicle_type=='car':
                self.vehicle=Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
                # print(f'vehicle {vehicle_type} is registered')
            elif vehicle_type=='bike':
                self.vehicle=Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
                print(f'vehicle {vehicle_type} is registered')
            else:
                self.vehicle=Cng(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
                print(f'vehicle {vehicle_type} is registered')


        else:
            pass
    def get_trip_history(self):
        return self.__trip_history

    def start_a_trip(self,start,destination,fare,trip_info):
        self.earning+=fare
        self.Location=destination
        #start multithreadding
        trip_thread=threading.Thread(target=self.vehicle.start_driving,args=(start,destination,))
        trip_thread.start()
        # self.vehicle.start_driving(start,destination)
        self.__trip_history.append(trip_info)
        
    
        

rider1=Rider('rider1','rider1@gmail.com','rider1sr',randint(0,30),1000)
rider2=Rider('rider2','rider2@gmail.com','rider2sr',randint(0,30),7500)
rider3=Rider('rider3','rider3@gmail.com','rider3sr',randint(0,30),8500)
rider4=Rider('rider4','rider4@gmail.com','rider4sr',randint(0,30),8500)
rider5=Rider('rider5','rider5@gmail.com','rider5sr',randint(0,30),8500)
# print(dir(rider2))
vehicle_type=['car','bike','cng']
for i in range(1,100):
    driver1=Driver(f'driver{i}',f'driver{i}@gmail.com','driver{randint(250,500)}',randint(0,30),randint(10000,99999),'0172571357')
    driver1.take_driving_test()
    driver1.register_a_vehicle(choice(vehicle_type),randint(10000,99999),10)   
uber.find_a_vehicle(rider1,choice(vehicle_type),randint(1,100))
uber.find_a_vehicle(rider2,choice(vehicle_type),randint(1,100))
uber.find_a_vehicle(rider3,choice(vehicle_type),randint(1,100))
uber.find_a_vehicle(rider4,choice(vehicle_type),randint(1,100))
uber.find_a_vehicle(rider5,choice(vehicle_type),randint(1,100))
# uber.find_a_vehicle(rider1,'car',randint(1,100))
# uber.find_a_vehicle(rider1,'car',randint(1,100))

print("rider1 avaiable balance",rider1.Balance)
print(uber.total_income())
print(rider1.get_trip_history())





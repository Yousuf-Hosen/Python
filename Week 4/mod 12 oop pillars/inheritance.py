""" laptop,phone,watch,tablet """

# inheritance create a common classs
# base class will have only common attributes and methods
""" 
1.single level inheritance(parent ---> child)
2.multilevel inheritance(grandpa-->father--->chhild)
3.multiple inheritance(father,mother:child(father,mother))
4.heiarchy inheritance(father: father-->you,father-->your brother,father--->your sister)
 """

class Device:
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color

    def re_sale(self):
        print("this device is ready to sale again")

class Laptop(Device):
    def __init__(self,brand,price,color,disc_size):
        super().__init__(brand,price,color)
        self.disc_size=disc_size
    def __repr__(self) -> str:
             
            return f' Laptop {self.brand} : {self.price} : {self.color}'
       
    def rub(self):
        print("running the device")
    def purchase(self,money):
        if money<self.price:
            return ' No laptop for you in this price range'
        else:
            print("this device is for you")
            return money-self.price
   
class Phone:
    def __init__(self,brand,price,color,camera,batary,sim_num):
        self.brand=brand
        self.price=price
        self.color=color
        self.camera=camera
        self.batary=batary
        self.sim_num=sim_num
    def is_dual(self):
        if(self.sim_num>1):
            print("Its dual sim")
        else:
            print("its nano sim")
    def __repr__(self) -> str:
        return f'The Phone is {self.brand} : {self.price} : {self.color} : {self.camera} : {self.batary} : {self.sim_num} '
            
class Watch:
    def __init__(self,brand,price,color,watch_type):
        self.brand=brand
        self.price=price
        self.color=color
        self.watch_type=watch_type
    def is_digital(self):
        self.watch_type=="Digital"


class Manager:
    def __init__(self,name,salary,experience,designation):
        self.name=name
        self.salary=salary
        self.experience=experience
    def day_total_sales(self):
        pass
    def handle_customer_complaine(self):
        pass
    def withdraw_salary(self):
        pass

class SalesPerson:
    def __init__(self,name,salary,experience,designation,commision):
        self.name=name
        self.salary=salary
        self.experience=experience
        self.designation=designation
        self.commision=commision


    def withdraw_salary(self):
        pass
lenovo=Laptop("Lenevo",42000,"Blue",'500GB')
HP=Laptop("HP pavilion",35000,"Black",'520GB')
print(lenovo)
print(HP.brand)


oppo=Phone("OPPO F23",23000,"Black","12MP",5000,2)
Samsung=Phone("Samsung A53",39000,"Golden","15MP",5000,3)
print(oppo)
print(Samsung)

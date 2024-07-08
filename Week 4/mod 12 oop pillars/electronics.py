""" laptop,phone,watch,tablet """
class Laptop:
    def __init__(self,brand,price,colour,disc_size):
        self.brand=brand
        self.price=price
        self.colour=colour
        self.disc_size=disc_size
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

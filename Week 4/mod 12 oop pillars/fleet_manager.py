class Bus:
    owner="Ena poribohon"
    def __init__(self,route,license,driver):
        self.route=route
        self.license=license
        self.driver=driver
        self.trips=[]
    def start_strip(self,start_time):
        self.trips.append(start_time)
class Driver:
    def __init__(self,name,age,phone,license,address,salary):
        self.name=name
        self.age=age
        self.phone=phone
        self.license=license
        self.address=address
        self.salary=salary

        pass
    def drive(self,start,end):
        pass
    def take_vacation(self):
        pass
    def withdraw(self):
        pass
class Passenger:
    def __init__(self,name,phone,start,destination):

        pass
    def purchase_ticket(self,destination,money):
        pass
class Manager:
    def __init__(self,name,phone,department):
        pass
class Counter:
    def __init__(self,place,manager):
        pass

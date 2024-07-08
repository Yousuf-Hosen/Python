""" 
                    Parking LOt Design using python OOP
                    1.Display spots available on parking lot
                    2.Park their car in the parking lot
                    3.Remove car from parking lot
Car class : 1.License
            2.Model of Car
            3.car_colour
            
Garage class:
            1.Spot available()
            2.add car()
            3.remove_car()-> bill payments
            4.show_cars()
 """
class Car:
    def __init__(self,License_no,Model_no,car_color):
        self.License_no=License_no
        self.model_no=Model_no
        self.car_color=car_color
    def __repr__(self):
        return f'{self.License_no},{self.model_no},{self.car_color}'

# __repr__ -> formal_strings, not readable format
#str(__repr__) -> readable format strings

class Garage:
    def __init__(self):
        self.Car_added=[]
        self.Spot=10
        self.Car_info={}
        self.bill=0
        self.ticket=[]
    def Spot_available(self):
        return self.Spot
    
    def Add_car_to_garage(self,Car_obj):
        #    print(Car_obj)
           self.spot_name=['A1','B1','C1','D1','E1','F1','G1','H1','I','J']
           if self.Spot_available()>0:
               user_data=str(Car_obj).split(',')
               print(user_data)
               self.Car_added.append(user_data)

garage=Garage()
user_car=Car('TAN123','Ferrari12','Red')
garage.Add_car_to_garage(user_car)

               
        

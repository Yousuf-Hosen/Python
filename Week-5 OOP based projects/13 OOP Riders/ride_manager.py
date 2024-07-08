class RideManager:
    def __init__(self):
        print("Ride Manager activated")
        self.__availableCars=[]
        self.__availableBikes=[]
        self.__availableCngs=[]

    def add_a_vehicle(self,vehicle_type,vehicle):
        if vehicle_type=='car':
            self.__availableCars.append(vehicle)

        elif vehicle_type=='bike':
            self.__availableBikes.append(vehicle)
        else:
            self.__availableCngs.append(vehicle)
    def get_available_cars(self):
        return self.__availableCars


    def find_a_vehicle(self,rider,vehicle_type,destination):
        print("Looking for a good morning")
        if vehicle_type=='car':
            if len(self.__availableCars)==0:
                print("Sorry no cars are available")
                return False
            for car in self.__availableCars:
                print('potential riders at-> ',rider.Location," ",car.driver.Location)
                if abs(rider.Location-car.driver.Location)<10:
                    print("Find a match for you")
                    return True


uber=RideManager()

    


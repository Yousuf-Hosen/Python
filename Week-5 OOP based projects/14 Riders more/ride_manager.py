class RideManager:
    def __init__(self):
        print("Ride Manager activated")
        self.__income=0
        self.__trips_histry=[]
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

    def total_income(self):
        return self.__income
    def trip_history(self):
        return self.__trips_histry
    def find_a_vehicle(self,rider,vehicle_type,destination):
        # print("Looking for a good morning")
        if vehicle_type=='car':
            vehicles=self.__availableCars
        elif vehicle_type=='bike':
            vehicles=self.__availableBikes
        else:
            vehicles=self.__availableCngs

        if len(vehicles)==0:
            print("Sorry no cars are available")
            return False
        for vehicle in vehicles:
            # print('potential riders at-> ',rider.Location," ",car.driver.Location)
            if abs(rider.Location-vehicle.driver.Location)<10:
                distance=abs(rider.Location-destination)
                fare=distance*vehicle.rate
                if rider.Balance<fare:
                    print(f"your fare is {fare} and you have {rider.Balance}")
                    return False
                
                if vehicle.status=='available':
                    vehicle.status='unavailable'
                    trip_info=f"found matched {vehicle_type} for {rider.name} for fare {fare} with {vehicle.driver.name} from started {rider.Location} to destination {destination}"
                    print(trip_info)
                    vehicles.remove(vehicle)
                    rider.Start_a_Trip(fare,trip_info)
                    vehicle.driver.start_a_trip(rider.Location,destination,fare*0.8,trip_info)
                    self.__income+=fare*0.2
                    self.__trips_histry.append(trip_info)
                    
                    return True


uber=RideManager()

    


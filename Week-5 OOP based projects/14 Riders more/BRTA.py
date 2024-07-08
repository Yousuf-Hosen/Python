import random
class Brta:
    def __init__(self) -> None:
        self.__license={}
    
    def Take_Driving_test(self,email):
        score=random.randint(0,100)
        if score>=33:
            # print("congrats you hav passed",score)
            license_number=random.randint(5000,9999)
            self.__license[email]=license_number
            return license_number
        else:
            # print("Sorry, you are failed in driving test ", score)
            return False
    def Check_license(self,email,license):
        for key,value in self.__license.items():
            if key==email and value==license:
                print("matched")
                return True
        return False
    
                


     



        



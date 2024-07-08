""" All about mankind """

class Human:
    def __init__(self,gender,height,weight):
        self.gender=gender
        self.height=height
        self.weight=weight
class Police(Human):
    def __init__(self, gender, height, weight,nationality,cases):
        super().__init__(gender, height, weight)
        self.nationality=nationality
        self.cases=cases

class CS_Engineer(Human):
    def __init__(self,love_to_code,Has_Gf, gender, height, weight):
        super().__init__(gender, height, weight)
        self.love_to_code=love_to_code
        self.Has_Gf=Has_Gf

if __name__=='__main__':

 police_man=Police("Male",65,56,'Bangladeshi',True)
 print(police_man.gender)
 print(police_man.height)
 Cs=CS_Engineer('YES',False,'Male',54,48)
 print(Cs.height)


        
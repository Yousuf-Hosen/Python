#poly=many
#morp=differnt
class Animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("The Animal was making sound")


class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("Bark bark")


class Cat(Animal):
    def __Init__(self,name):
        self.name=name
    
    def make_sound(self):
        print("Meow meow")

class Pet(Animal):
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print("My pet is sounding")
class posu(Animal):
    def __init__(self,name):
        self.name=name
    

dog=Dog("rana vaii")
dog.make_sound()

cat=Cat("Akash bro")
cat.make_sound()

pet=Pet("Rakibba")
pet.make_sound()

po=posu("Amirra")
po.make_sound()

    
   
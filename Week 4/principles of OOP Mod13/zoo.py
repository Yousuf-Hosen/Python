# Abstract class
from abc import ABC,abstractmethod
# abc--> abstract base class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass


    
    @abstractmethod
    def move(self):
        print("animal is the creation of Allah")
class Monkey(Animal):
    def sing(self):
        print("Monkey is singing")

    def __init__(self):
        self.__name="Monkey"
        
    def eat(self):
        print("monkey is eating banana")
    

    def move(self):
        print("The monkey laughing around the field")
        super().move()
    

    @property
    def name(self):
        return self.__name
    
    # set the property as you wish
    @name.setter
    def name(self,value):
        self.__name=value
    


class Tiger(Animal):
    def attack(self):
        pass
    def speed(self):
        pass
    
  


layka=Monkey()
print(layka)
layka.sing()
layka.eat()
layka.move()
layka.name="white monkey"
print(layka.name)
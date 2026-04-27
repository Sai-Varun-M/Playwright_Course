#abc - Abstract Base Class
from abc import ABC,abstractmethod

#Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("started")
    
    @abstractmethod
    def stop(self):
        pass

#Concrete class(implement from abstract methods from abstract class)
class Car(Vehicle):
    def start(self):
        print("Car engine started...")
    
    def stop(self):
        print("Car engine stopped...")


c=Car()
c.start()
c.stop()

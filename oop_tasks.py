

class Rectangle : 
    def area():
     return self.width*self.length     
    def __init__(self,len,wid) :
        self.length=len
        self.width=wid

 
#Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self,max,mile):
        self.max_speed=max
        self.mileage=mile
#Create a Vehicle class without any variables and methods.
class Vehicle:
    pass
        
#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class 
class Child(Vehicle):
   pass
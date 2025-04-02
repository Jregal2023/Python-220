#inheritance and polymorphism
#inheritance - inherit a class and all of its methods and data
#polymorphism - means overriding behavior in derived/child classes. more generally polymorphism means that something does the 
#same thing, but how they do it is different

#a class that is called shape, but to calculate area is different depending on the shape
#ie a square and a circle have different formulas for calculation but they are still calculating area

class Vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("MOVE YO ASS")

#We can inherit this to other classes. we inherit when things aare something
#is a relationship
#you should never (Hamby rule) derive more than one class deep

#create a class called car that inherits from vehicle
class Car(Vehicle):
    #car will take in every attribute and function from vehicle, which means we dont have to create a constructor
    #function UNLESS we need to add mroe data besides model and brand

    #however, our car can move, but the way it moves is different. It goes Vroom vroom
    #therefore we can override the move method/ function
    def move(self):
        print("vroom, vroom")

class Plane(Vehicle):
    def move(self):
        print("FLY")

class Boat(Vehicle):
    #we have a new data field here we want to add called type - like a speed or fishing boat
    def __init__(self, brand, model, boatType):
        #inherits from the base or super class which is vehicle
        super().__init__(brand,model)
        self.boatType = boatType

    def move(self):
        print("Sail")

car = Car("Ford", "Mustang")
plane = Plane("Boeing", "747")
boat = Boat("Ibiza", "Touring 20", "Speed Boat")

car.move()
plane.move()
boat.move()
"""
M03 Lab: classes and inheritance/ Jregal 
Write a Python app that has the following classes:

    A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
    A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
        year
        make
        model
        doors (2 or 4)
        roof (solid or sun roof).
    Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
    The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
    The app will then output the data in an easy-to-read and understandable format, such as this:
      Vehicle type: car
      Year: 2022
      Make: Toyota
      Model: Corolla
      Number of doors: 4
      Type of roof: sun roof"""

#super class for the Automobile which gets the vehicle type
class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType
    


#class that gets the value it does this through displayDetails which display when getting the value __init__ from function
class AutoMobile(Vehicle):
    #__init__ 
    def __init__(self, vehicleType, year, make, model, doors, roof):
        super().__init__(vehicleType)
        self._year = year
        self.__make = make
        self.__model = model
        self.__doors = doors
        self.__roof = roof
    #displays the details of the vehicle including vehicleType, year, make, model, doors, roof   
    def displayDetails(self):
        print("Vehicle type: ", self.vehicleType)
        print("Year: ", self._year)
        print("Make: ", self.__make)
        print("Model: ", self.__model)
        print("Number of Doors: ", self.__doors)
        print("Type of roof: ", self.__roof)

#inputs used for the automobile
vehicleInput = input("Enter the vehicle what it is: ")
yearInput = int(input("Enter the year of the model: "))
makeInput = input("The Maker of the vehicle: ")
modelInput = input("The Model of the vehicle: ")
numOfDoors = int(input("Enter the number of doors (2 or 4): "))
roofInput = input("Enter the type of roof (solid or sun roof): ")

# prints out the results of the class
car = AutoMobile(vehicleInput,yearInput,makeInput,modelInput,numOfDoors,roofInput)
#car.__init__(vehicleInput,yearInput,makeInput,modelInput,numOfDoors,roofInput)
print("Car Details:")
print(car.displayDetails())
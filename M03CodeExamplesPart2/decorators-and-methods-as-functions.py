# in Python, a decorator is a function that takes another function in as input, and extends or modifies its behavior
#without explicitly modifying the original function code
#this is a cool way to add functionality to existing functions/classes, and promotes code reusability

#in simple terms, a decorator is a "wrapper" for a function that adds code to the function in order for it to do something more

#an example would be routes in django
#a route ties a URL to a function
#the decorator would grab the url and then take in a function as an arguement to be ran when someone visits the url
#really good for event programming

def my_decorator(func):
    def wrapper():
        print("Something after the function")
        func()
        print("Something after the function")
    return wrapper

#to create a function that uses a decorator use the @nameofdecorator before defining function

@my_decorator
def sayHello():
    print("hello")

sayHello()

#lets say we want to create a class for someone else to use like a module or a library
#but that class is really only a list of functions we can use
#think of a math utilities class - a group of functions that can do calculations
#we can use classes to also just be a way to group functions together using static methods decorator
#static methods - only functions no data

class MathCalcs:
    @staticmethod
    def add(x,y):
        return x + y
    @staticmethod
    def multiply(x,y):
        return x * y
    
sum = MathCalcs.add(10,5)
print(sum)
product = MathCalcs.multiply(10,8)
print(product)
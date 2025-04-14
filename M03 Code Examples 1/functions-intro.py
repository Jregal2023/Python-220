#all the following describe a function
#methy - functions take in data, transform it, then output a result
#functions are considered actions - verb
#SDEV definition - functions are blocks of code that can be repeated when called, it can have data passed to it
#and *can* return data as a result

#we already ahve used functions before - print() and input()
#if we want to make a "custom" function, we have to define or create a template for it
#in python we call our own custom functions defined functions

#two step process to defining and using functions
#defin a function like a template to be used later on -- keyword def functionName():
#Def functionName():

#lets look at all they wats functions can be used from an intro standpoint
#functions can be used as a summary of statements and not return value
#often called void functions
#example below is we take to numbers and add them together
def myFunc():
    x = 6
    y =7
    sum = x + y
    print(sum)

#to use or call a function we just type its name followed by ()
myFunc()
myFunc()

#we often use functions so we can pass data to it 
#parameters - variables that are passed to a function
#parameters are just an argument that we have not used yet and defined when defining a function
#reminder - an argument is what we use when running a function and passing data : print ("My name is Jace")
#paramaters are placed inside the parenthesis of the define dfunction
#passing data - giving the function some outside data to process
#We can pass any data type we ant to the function including data structures like lists
#in python we can also pass data to other functions.. this is known as higher order function or functions as first class 
#citizens ie in(input())  ie changing function

def displayNum(number): #you can think of parameters as placeholders for data.
    print(number) # whatever you place as a parameter in the (), the block of code below it will display

#when calling the function, the argument does not have to be the same name as the parameter
#the parameter is just there to tell the function what to do with the data

number = 10
displayNum(number)

#multiple parameters seperated by a ,
def addNumbers(num1,num2):
    sum = num1 + num2 
    print(sum)

addNumbers(7,8)
number1 = 10
number2 = 44
addNumbers(number1, number2)

#order matter with parameters
def divideNumbers(num1,num2):
    quotient = num1/num2 
    print(quotient)

divideNumbers(10,2)
divideNumbers(2,10)
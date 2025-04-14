#variables store data
#python is weakly typed you do not have to declare a data (int,float,etc...) type

#int - whole number
#float - decimal
#strings - text
#boolean - T/F

x =6 #int
y= 6.5 #float
name = "Jace" #string
myBool = True #bool true
falseBool = False #bool false

#functions - perform actions, take input, process input, and produce an output
#functions are the verbs of the programming world, they perform actions and processing
#we will use built in python functions at first. you can denote a function by have a ()
#arguments ar ethe data that goes in the (). they are used as part of the functions process to calculate or use

#input function - take an input and return it into a variable.
#the argument we stick inside the () in an input function is the prompt or text the user sees when asking for input

myName = input("What is your name?")
#print function - displays something on screen. The argument is the thing you want to display
print("Your name is" , myName)

#the cool thing about variables is that they can change, and you can also use the current value of the variable in
# its own calculation
z = 6
z = z + 4
print(z)
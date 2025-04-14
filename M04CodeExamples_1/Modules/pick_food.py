#modules allow us to break an application into pieces
#we use modules to work on projects collaborativly as well as maintain our code through various files
#it allows us a separation of concern.

#we will make a quick app that will randomly pick froma  list of restaurants to go to.

#things we need to know
#1 - how to grab a module from an outside library or the standard library from python
#2 - hot to implement our own custom modules 

#to import any module or package we use the import keyword
#we are going to import from the random library/module/package from the standard python package
#random can create a series or random numbers or pick a random item from a list
# we will also us the keyword from to grab the library and call the functions we want to use

from random import choice

#list of restauraunts
places = ["Mcdonalds", "Taco bell", "Culvers", "Popeyes"]

#this file will be used as a module for other files... therfore we need a function to do something in the other file
#we will create a pick function that runs the choice function against this list

def pick():
    return choice(places)

myFood = pick()
print(myFood)
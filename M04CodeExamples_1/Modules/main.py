#we are going to import pickFood into our main file

#there are multiple ways to import a module

#first way is to import everything without using an alias 

#an alias is importing a function or class and naming it something else in the file
#import pick_food

#second way is to give it an alias where we change the name of the local import into something else
#import pick_food as mypick
#place = mypick.pick()

#place = pick_food.pick()

from pick_food import pick
place = pick()
print(place)



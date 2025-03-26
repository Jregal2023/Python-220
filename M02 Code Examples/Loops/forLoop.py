#for loop repeats code a certain number of times

#python is a little weird with for loops... There are several to do it, but in other languages, this is the traditional way

#for(int i = 0, i < 10; i++)
#i is just a short hand for iterator
#iterator is the value that keeps up with the current loop number
#iteration means to go through a loop or a cycle

#python uses a range function to take care of the iteration values
#for in loop - for blank in blank. for i in number of loops
#syntax for iteratorName in range(startingValue, endingValue, increment/decrement)

number = 5

for i in range(0,number,1):
    print(i)

print("*********************************")

#decrements - use negative values

countdown = 0

for i in range(10, countdown, -1):
    print(i)
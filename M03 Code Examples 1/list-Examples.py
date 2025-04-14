#data structures define how data is stored and organized outside of normal(primitive) data types (ie float string int)
#usually they contain more than one piece of dta
#python simplist data structure is know as a list
#this is similar to an array in other languages with some differences
#lists are dynamic in size (ie not fixed size)
#lists contain multiple data types inside (usually don't do this)
#lists are mutable - they can change after they are created, and items inside of it can be deleted, modified or changed

#create a list syntax
#nameoflist = []
#a list can be empty or initizalized with values

#create a list with some data in it for test scores
#the reason why we use a list in the first place is to mdify data dynamically and organize like item

testScores = [100,95,77,85]
#each item in list is seperated by a comma
#to access items in a list you say listname[index]
#index is the order/position of an item in a list
#start at 0... in the above example 100-0 index, 90-1 index, 77-2 index, etc....
print(testScores[1])
print(testScores[0])

#another advantage of a list is the ability to use loops to process data
#if we need to display something in a list we can either call the single item we need or call all items using a loop
#for in loop - counts the number of items and loops through that list that same number of times

#syntax for varnamethatrepresentsasingleitem in listname
for testScore in testScores:
    print(testScore)

#modify things in a list and modify more than one thing at a time

for testScore in testScores:
    testScore = testScore + 5
    

    print(testScore)

print(testScores)


#you can add data to a list by using the append function

newScore = 65
testScores.append(newScore)
print(testScores)

#creating a new list based on an old list or add data to anew list

newTestScores = []
for testScore in testScores:
    testScore = testScore +5
    newTestScores.append(testScore)
    print(testScore)

print(newTestScores)

#combine lists together
#extend() combine data from one list to another
testScore2 = [95,80,88]
testScores.extend(testScore2)
print(testScore2)

#remove the first instance of a value from a list
testScores.remove(88)
print(testScores)

#finding something in a list - we wil lfirst create a value that will look for the item we are looking for in the list

lookingFor = 80
#use the in keyword to find something is in a list
found = lookingFor in testScores
print(found)

if found == True:
    print("Found the value")
    testScores.remove(lookingFor)
    print("Removed")
print(testScores)

#checking to see if there is more than one instance of a value
print(testScores.count(95))

#sort a list - ascending order aka smallest to largest
num = [5,1,10,8,6,3]
num.sort()
print(num)

#sorting in desc order - largest to smallest
num.sort(reverse=True)
print(num)

#check to see how many items are in the list aka length
print(len(num))

#using len() function we can actually iterate over the list using a more traditional approach where we may need an index value

for i in range(len(num)):
    print(i, "-", testScores[i])
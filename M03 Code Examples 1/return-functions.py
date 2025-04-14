#functions can also return values int ovariables or other functions
#return value = the value is return to something outside of the function ()often a variable
#we use the keyword return to do so

#it is not to much different from a void function, we are jsut going to return the data into something else

def addItems(item1,item2,item3):
    total = item1 + item2 + item3
    return total # you should only return one value

myTotal = addItems(1,2,3)
print(myTotal)

#chain functions together as long as the inner function is a return function
#lets take the total from the addItems functions and add sales tax
def addTax(total):
    tax = total * 0.10 
    totalWithTax = total + tax
    print("Your total with tax is", totalWithTax)

#chain the functions together - add items has a return value. that return value is one single thing that can then be used
#by the addTax function
addTax(addItems(5.00,10.00,7.00))

#we can also use functions with more complicated data types like lists
groceries = ["orange", "milk", "butter"]
numbers = [1,2,3,4]

def printList(aList,value):
    for item in aList:
        print(item)

def subtractList(aList,value):
    for item in aList:
        item = item - value
        print(item)

printList(groceries)
printList(numbers)
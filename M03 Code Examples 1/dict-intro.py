#dictionaries create key-value pairs that can associate a name(key) witha value
#python treat dictionaries like objects or maps
#object has properties()characteristics to describe usually a thing or a group of related characteristics
#ie a Person has a name and an age
#an object or dict can mix data types

#objects can be almost anything but in programming it usually means or usually refers to a wrapper that encasuplates related data together
#Person - name,age
#Car - make, model, yearsCreated

#dictionaries can be treated like objects in python, we just organize the data differently
#in dict we can group something by a list of items and associated values like a list 
# (ie. just like a regular dictionary with terms and definitions)
#lets look below for an example using a list of customers and their bank balance
#dict syntax - dictname{Key:value, key:value}
bankCustomers ={
    #key is a string surrounded by quotes
    "Alice" : 100,
    "Tim" : 200,
    "Sam" : 500
}

#to loop or access dictionaries, we can access them by their key
for customer in bankCustomers:
    #customer is the key and the index.. we can print the keys name, and then access the alue by calling the dict
    #name using customer as an index
    print(customer, bankCustomers[customer])

#use dict like an object - they are basically the same thing in python .. just organize data differently
#when we organizae data in this way, the keys are often called properties or fields
#they describ the single object and its characteristics
personJace = {
    "Name": "Jace",
    "Age" : 20,
    "City": "Indy"
}

for details in personJace:
    print(details, ":", personJace[details])

#adding data is pretty easy. There is no function you need to run, just need to call the dict and add a new key name with the 
#[]
#if the keyname does not exists, it will add it to the dict
#BE CAREFULL - if the key name does exist, it will overrite the value
bankCustomers["Jace"] = 400
print(bankCustomers)
#modifying consistent data
bankCustomers["Alice"] = 900.00
print(bankCustomers)

#grab a single item and display its value you can also use the get() with the key name
print(bankCustomers.get("Alice"))

#delete items from dict using del keyword.. looks different than a function
del bankCustomers["Alice"]
print(bankCustomers)

#finding items in a dict is similiar to a list...use in keyword
key = "Tim"
if key in bankCustomers:
    print(key, "is in the dictionary")
else:
    print("Not in the dict")

#maybe you want your search to be more detailed... ie the key and value both match
findName = "Tim"
value = 200.00

#loop to do this
#for keyname, valuename in dictname.items()
for name, balance in bankCustomers.items():
    if name == findName and balance == value:
        print(findName, "has a balance of ", value)
    #else:
     #   print("Customer not found")
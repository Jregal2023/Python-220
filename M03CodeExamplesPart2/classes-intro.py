#classes are similiar to us combining a data structure like a dict with functions.
#but it also will allow us to create copies of these structures(instances) that maintain seperate data values
#while maintaining the same type of data.

#wha tis a class - a blueprint for an object that contains data (attributes/fields) and functions(methods)
#methods are pretty much the same thing as functions, but they must be part ofa class or object. 
#we use (.) notation to access an objects methods

#instance = copy or spawn of a class. COncrete manifistation of that class. A object is very flexible and can be made almost any way you wish

#object usually represent real world things or collections of data (ie person, dog, accounts, etc..)

#to use a class we must first define it similiar to a function
#we use keyword class

class Person: 
    #attributes/fields
    name = "Jace"
    age = 20


#classes are like blueprints. We can use variables within a class to act as a "Master copy" that can be overriden
#when we make an instance of that class

#when we us a class we call this making an instance or instantiating

instance1 = Person() #create the instance of the class above

#to access fields inside of the class we use dot notation
print(instance1.name)
print(instance1.age)

#we can make any instances of the class we want
instance2 = Person

instance2.name = "Tim"
instance2.age = 49

print(instance2.name)
print(instance2.age)

#even though we use the same class as a blueprint, the data is different between instances of that class.
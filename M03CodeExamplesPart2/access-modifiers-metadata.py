



class BankAccount:

    def __init__(self,name, balance):
        
        #we want to get the name

        self.___name = name
        self.___balance = balance

#this means we cannot access or change any day without first creating a function to access that data
#this seems redundant at first or overly complicated, but it allows us to create like name functions
#between classes that do the same thing
#it allows for us to create unstance of a class in other classes and have them only have access to certain functions or data

#we often call this methods to grab or change data getters and setters
    def get_name(self):
        return self.___name
    
    def get_balance(self):
        return self.___balance
    
    def set_name(self, name):
        self.___name = name

    def set_balance(self, balance):
        self.___balance = balance

#you should also think about what functions would be useful for your class
    def deposit(self,balance):
        self.___balance = self.___balance + balance

    def withdraw(self,balance):
        self.___balance = self.___balance - balance


acct1 = BankAccount("Jace", 400.00)
print(acct1.get_name())
print(acct1.get_balance())

acct1.set_name("Tim")
acct1.set_balance(8000.00)

acct2 = BankAccount("Joe", 700.00)
acct2.deposit(200.00)
#acct1 balance has not been changed since we chat it to Tim and 800.00 because our instances have different data values inside
print(acct1.get_name())
print(acct1.get_balance())

acct2.withdraw(300.00)
print(acct2.get_balance())
#nested if works by having a series of it statements that must be true, and then drilled down to the vaue you are looking for
#compound conditions and elif statements can help relive some of this
#lets create a quick program that will say you get a discounted movie if you are 12 and younger or if you are a senior citizen

# We use nested ifs to check for multiple conditions

ticketPrice = 10.00
discount = 0.10

age = int(input("Give me your age "))
rating = "G"

if(rating == "G"):
    if age <= 12:
        ticketPrice = ticketPrice - (ticketPrice * discount)
        print("Child discount. Your ticket price is", ticketPrice)
   
    if(age >= 65):
        ticketPrice = ticketPrice - (ticketPrice * discount)
        print("Senior citizen discount. The ticket price is", ticketPrice)
    if(age >= 13 and age <= 64):
        print("No child or Senior citizen discount", ticketPrice)

else:
    print("Move is not rated G, pay full price", ticketPrice)

#there are several ways to do this however this is one of the easier ones


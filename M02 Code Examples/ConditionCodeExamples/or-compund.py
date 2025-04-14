# lets use the movie program from earlier but clean it up with an or statement

ticketPrice = 10.00
discount = 0.10

age = int(input("How old are you: "))

if age <= 12 or age >= 65:
    ticketPrice = ticketPrice - (ticketPrice * discount)
    print("you are able to get a discount", ticketPrice)
else:
    print("Pay full price", ticketPrice)


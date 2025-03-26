#loops are also control structures. They repeat code untril the condition is met. 
# They use the same logic and relational operators as if statements

#loops main goal is to repeat code until you do not want this code repeated
#two types of loops - while and for

#while loop - is a loop that repeats code until a specifc condition is met (usually using a flag or a sentinel value)
#and then is broke when the condition is met

#for loop - does a similiar thing, but is a count controlled loop. 
# It is controlled by a counter and repeats a certain number of times and then exits

#while loop are usually broke by a flag value that is changed inside the body of the loop when you ned the loop broken

#flag/sentinel value
keepGoing = "y"

#make a commision program to check to sales and commission.. breaks when the user is done with the program

while(keepGoing == "y"):
    sales = float(input("Please give me your sales for the month "))
    comRate = float(input("What is your commission rate in decimal form "))
    totalEarned = sales * comRate
    print("You have earned", totalEarned, "this month")
    keepGoing = input("Do you wish to run again? if so press y and enter. Otherwise press any other letter and enter to"
    "exit")

print("Thanks for using our program")
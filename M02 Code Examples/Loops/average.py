#use loops as an accumulator(ie keep up with running values or totals)
#this program will average numbers

totalSum = 0
average = 0

howManyNumbers = int(input("How many numbers do you wish to average? "))


for i in range(0, howManyNumbers, 1):
    value = float(input("Please enter your value #: " ))
    totaSum = totalSum + value

print("Your total sum is", totalSum)
average = totalSum / howManyNumbers
print("Your average is", average)

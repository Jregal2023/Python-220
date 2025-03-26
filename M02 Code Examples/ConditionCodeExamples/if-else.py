#if-else are called dual alternative. Means two paths to choose from


a = 7
b = 9

if a == b:
    print("These are equal")
else:
    print("These are NOT equal")

#evaluating strings with if-else
message = "yes"

if message == "yes":
    print("You said Yes")
else: 
    print("NOOOOOOO!!")

# see if you can vote ... we are only checking to see if someone is 18 or older

age = int(input("Please give me your age: "))

if age>= 18:
    print("You can vote")
else:
    print("You cannot vote")
#compund operators allw you to check for multiple conditions inline with our if statements
# there are three types of compound operators

#and - both if conditions must be true for the code to execute
#or - only ONE condition must be true for the code to execute

#not - flips the result of your conditions boolean value (ie true becomes false...false becoems true)

#truth tables
#compare booleans to get a result

#And Truth table
#T/T = True
#T/F = False
#F/T = False
#F/F = false

#or TT 
#T/T = T
#T/F = T
#F/T = T
#F/F = F

#take an example of the voting program and add registered voter
age = 19
registered = "y"

# and both must be true
if age >= 18 and registered ==  "y":
    print("You Can Vote")

elif age >= 18 and registered == "n":
    print("Your old enough to vote, but not registered")
elif age <= 17 and registered == "y":
    print("You are registered, but not old enough to vote")

else:
    print("You are neither old enough, nor are you registered, you cannot vote")
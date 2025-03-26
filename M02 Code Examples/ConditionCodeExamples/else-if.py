#muli-alternative more than 2 branches
#Usually deals with ranges or deals with ahavign multiple conditions to check
#to do this we use else-if statemetns. in python elif

#below is an example of using elif statements to change numerical grades into letter grades (Think like a gradebook)
#ie - A = 90-100, B = 80-89, C = 70-79 etc...

numGrade = 80
letterGrade = ""

if numGrade >= 90:
    letterGrade = "A"
    print("Your grade is,", letterGrade)
#well 80 is greater than 70, why does my letter grade not change to C
#short-circuit evaluation
#as soon as a condition is met, it exits the elif structure
elif numGrade >= 80:
    letterGrade = "B"

elif numGrade >= 70:
    letterGrade = "C"

elif numGrade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print("Your grade is,", letterGrade)
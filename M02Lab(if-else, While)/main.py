'''Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. Your app will:

    ask for and accept a student's last name.
    quit processing student records if the last name entered is 'ZZZ'.
    ask for and accept a student's first name.
    ask for and accept the student's GPA as a float.
    test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
    test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
'''

print("Enter the students first, and last name, as well as their GPA ")

lastName = ""
while True:
   
    print("Enter the students first, and last name, as well as their GPA ")
    
    lastName = input("Enter the lastname, or ZZZ to quit program ")
    if(lastName == "ZZZ"):
        print("Thank you have a good one")
        break
    firstName = input("Enter the firstname ")
    GPA = float(input("Enter the students GPA "))

    if GPA >= 3.5:
        print("The student can enter the Dean's List!")
    
    elif GPA >= 3.25:
        print("The Student can enter in Honor Roll!")
    
    else:
        print("The Student does not qualify for either ")
    
   
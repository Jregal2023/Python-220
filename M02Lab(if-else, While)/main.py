'''This is programs purpose is to enter students' enter their gpa, as well as their first and last name. 
The program is made up of a while loop in which if you wish to cancel the program type ZZZZ
'''

print("Enter the students first, and last name, as well as their GPA to see if they qualify for either Honor Roll, Deans' list, or niether")

lastName = ""
while True:
   
    print("Enter the students first, and last name, as well as their GPA. If you wish to quit type ZZZ in lastname ")
    
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
    
   
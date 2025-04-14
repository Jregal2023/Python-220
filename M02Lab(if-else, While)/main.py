'''This is programs purpose is to enter students' enter their gpa, as well as their first and last name. 
The program is made up of a while loop in which if you wish to cancel the program type ZZZZ
'''
# programmed by Jace Regal 03/26/2025 as part of SDEV 220 M02 Lab If,else While 

#used to store the value of lastname, also used to ensure that the While loop can end when type ZZZ
#First name stores the string value of the students firstname, and GPA is a float that determines which category they fit.

#runs until lastname = "ZZZ"
'''Test cases:
lastName : Regal, firstName : Jace, GPA: 3.75
lastName : Hamby, firstName : Zachary, GPA: 5.0
lastName : Tharpe, firstName : Lucien, GPA: 1.4
lastName : Quinn, firstName : Caleb, GPA: 3.3
lastName : Hernandez, firstName : Kim, GPA: 3.6

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
    
   
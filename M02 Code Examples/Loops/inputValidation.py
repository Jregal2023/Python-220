#asks if you agree to terms and service... if not keep asking

#you can also use boolean values as flags.. just use the word True or False

while True:
    accept = input("Do you accept terms and Service? Press y and enter for yes")
    if accept != "y":
        print("Not Accepted.. you can't use our program until we own your soul")
    else:
        print("Thanks for accepting")
        break #breaks a loop
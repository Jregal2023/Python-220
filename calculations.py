
#the cool thing about variables is that they can change, and you can also use the current value of the variable in
# its own calculation
#addition
z = 6
z = z + 4
print(z)

#multiplication
x = 5
x = x *4
print(x)

#subtraction


#division

#int division -drops a decimal when dividing floats

decNum1 = 20.5
decNum2 = 10.3

intDivAnswer = decNum1 // decNum2
print(intDivAnswer)

#modul or modulus operator. Divides two number and the remainder is the resulting value
mod1 = 5
mod2 = 2
modAnswer = mod1 % mod2
print(modAnswer)

#exponents **
print(2 ** 8)

#string can only be added or concatonated (combined)
string1 = "8"
string2 = "9"
print(string1 + string2)

#all inputs come in a strings
#therfore you can't calculate them like normal
#so we have to convert those string to other numerical types like float or int
#there are built in functions to help us convert

# int() converts to int
# float() converts to float

#one of the cool things about python is that function are first class citizens
#this means that you can use functions insde of other functions
#chain functions

num1 = int(input("Give me your first number to add "))
num2 = int(input("Give me your second number to add "))
answer = num1 + num2
print(answer)


float1 = float(input("give me a number to multiply "))

float2 = float(input("give me a number to multiply "))

print(float1 * float2)
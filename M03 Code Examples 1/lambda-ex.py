#sometimes we want to easily create a function or use a function inside of another function
#we can actually create something called anonymous functions that have no name
#Why? 
#main reason is two fold
#1 - you can create variables a s function expressions.....
#expression is anything with a = sign for the most part 1 + 2 = 3 is an expression

#2 this is a very useful feature for even prorgramming, cuas eit reduces the steps

#event programming gui waiting on a button click... often ahve to have a minum of 2 to 3 functions
#function to wait on a button click - waitonbuttonclic(run another functuon on what to do when button is clicked)
#that means we need to create at least two functions
#problem is w edont care what the name of the function is that we want to run when the button is clicked.. we just
#want it to perform certain code

#function to make two numbers double 
def doubleNumber(number):
    double = number * 2
    return double

timestwo = doubleNumber(10)
print(timestwo)

#lambda function - use an expression =to define a function with an anonymous function. this derives from lambda calculus
#lambda functions are always return functions
#syntax varname = lambda parameter: function body
double = lambda number: number * 2

print(double(4))

#you can also use multiple params in an lambda
multiply = lambda firstNum, secondNum : firstNum * secondNum
print(multiply(7,5))

#we can also use lambda to make true anon functions if we just want to run some functions with params
word = "HelloWorld"

(lambda text: print(text))(word)



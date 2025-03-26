#if statements control the flow of a program by providing branching paths
#relations operator - ><==<=>+!=
#if statements are known as single alternatives - one branch

#if(condition):
a = 5

if a < 6:
    print("A is less than 6")

#double equal sign in a condition checks equality of two values
# do not use a single (=) equals sign because that is already reserved to assign values

c = 5
# == compares two things

x  = 7
y = 7
if y == x:
    print("X and Y are equal")

# != means not equal (not equal to something else.. what happens is that it takes a boolean and flips it)

mybool = True
mybool2 = False

t = 50
r = 22
if t != r:
    print("These are not equal")
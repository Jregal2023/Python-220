#tuples are what we call ummutable - does not change once declared
#lists of constants
#tuples are faster than lists
#you need a list of values that does not change or does not change often
#used for fixed data
#tuples have to be replaced to be changed(i.e. make a new tuple instead of replacing or modifying data in a list)

#first lets see how immutability works
#strings technically are immutable = you can change a string by replacing it in the variable name
#but you cannot replace each letter one at time

#name = "Zach"
#print(name)
#name = "Tim"
#print(name)
#name[0] = H will not work
#tuples are created using parenthesis = tuplename = (1,2,3,4)
#tuples can bea ccessed same way lists can and have a few of the same functions
states = ("IL", "IN", "KY")
#print tuples just like a list
for state in states:
    print(state)

#we needing to change more modify a typle, you can contanate or combien tuples
states2 = ("FL", "GA", "AL", "LA")
states3 = states + states2
print(states3)

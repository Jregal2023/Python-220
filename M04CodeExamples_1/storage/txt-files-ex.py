#text files are pretty eas to work in python... it allows us tos ave usntructured data

#create and write to a file
#open(filename, arguement for read, write, append)
#read = reads a file
#append - adds to existing files
#write - creates or overwrites a file

#create and write to a file
#create a variable that points 

file = open("myfile.txt", "w")
file.write("File now has text \n") #\n allows you to go to a new line
file.write("File has some more text")
#after winning you need too close the connection in case you need to use it again later
file.close()

#read a file
file = open("myfile.txt", "r")
#we have to grab each line for it to be read... there will be a simpler way to do this later
print(file.readline())
print(file.readline())


#you dont want read lines one at a time and call this repeatedly
#there are other utilities in python to help us
#with open is an example
with open("myfile.txt", "r") as myfile:
    while True:
        line = myfile.readline()
        if not line:
            break
        print(line)
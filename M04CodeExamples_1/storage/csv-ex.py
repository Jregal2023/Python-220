import csv
import pandas
#we can create our own csv files through objects and dicts

#csv of villians in comics using a list of lists
villians = [["Doctor", "Doom"], ["The", "Joker"], ["Oswald", "Cobblepot"]]

#we can use the csv package 
with open('villians.csv', "wt") as villianFile:
    csvout = csv.writer(villianFile)
    csvout.writerows(villians)

#pandas is a great library to read data from and we could do things like make charts or pretty displays
#we are just going to print data

data = pandas.read_csv('villians.csv')
print(data)
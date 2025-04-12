#import flask so we can use it
#from flask import Flask,request

#This is how we manipulate the database
#from flask_sqlalchemy import SQLAlchemy

#gets the name of the file
app = Flask(__name__)
#add our database
#there are several database software suites/server you can use ...MYSQL, postressSQL, SQL SERVER
#the most common into level -sqlite.... just a file that acts like a database

#configure our daatabase
app.config['SQLALCHEMY-']
db = SQLalchemy
#URI is ifferent then URL, its more foa resouce while URL has a website too!

#route decorator is a way for us to tue a route (url endpoint) to a function
#the route decorator (in the background) is grabbing the url and parsing it to something python can understand
#the function defined after the route then runs using the route as an endpoint

#route will take in one argument/param and that is the url path you wish to create
#if you just use a / that means the index page or home page

@app.route('/')
def index():
    return "Hello!"

#Make a route to query all the drinks in the databse
@app.rout('/drinks')
def get_drinks():
    #grabs all drinks
    drinks = Drink.query.all()
    #display th drinks
    output = []
    for drink in drinks:
        drink_data = {'name' = drink.name, 'description': drink.description}
        output.append(drink_data)
    return {"drinks" : output}

class Dring(db.Model):


    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(90), unique = True)
    description = db.column(db.String(120))

    #theo ther thing about models that is unique instead of jsut using raw SQL queries, is you cna add method or functions

    #one common one is the __repr__- function that when you call the name of a drink, it will return its name and description
    def __repr__(self):
        return f"{self.name} - {self.description}"
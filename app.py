from flask import Flask

#to see the result type "flask run" into the terminal

app = Flask(__name__)

@app.route('/') #<-- called "Decorator"
def home():
    return 'This works!'

@app.route('/inventory')
def inventory(): #<-- create a dictonary using JSON method/format (in postman use localhost5000:/inventory to access the dictionary)
    stock = {
        "stock":
        [
            {
                "name":"healing potion",
                "qty": 5,
                "price": 200
            },
            {
                "name":"speed potion",
                "qty": 2,
                "price": 500
            },
            {
                "name":"polymorph potion",
                "qty": 1,
                "price": 5000
            }
        ]
    }

    return stock
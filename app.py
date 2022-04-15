from flask import Flask, request
from staticModel import STOCK, getAllPotions, getPotionById

#to see the result type "flask run" into the terminal

app = Flask(__name__)

@app.route('/')#<-- called "Decorator"
def home():
    return 'You are now home'

@app.route('/inventory')
def inventory(): #<-- create a dictonary using JSON method/format (in postman use localhost5000:/inventory to access the dictionary)
    stock = {
        "potions": getAllPotions()
    }
    return stock

@app.route('/potions/<id>')
def potionByRoute(id):
    result = getPotionById(int(id))
    if result:
        return result
    else:
        return{"error":"No potion with that ID found."}

@app.route('/potions')
def potionByParam():
    id = request.args['id']
    result = getPotionById(int(id))
    if result:
        return result
    else:
        return{"error":"No potion with that ID found."}

@app.route('/potions', methods=['POST'])
def potionByPost():
    id = request.json['id']
    result = getPotionById(int(id))
    if result:
        return result
    else:
        return{"error":"No potion with that ID found."}

@app.route('/inventory/<catagory>/<id>')
def lookupItemByRoute(catagory,id):
    if catagory.lower() == 'potions':
        result = getPotionById(int(id))
        if result:
            return result
        else:
            return {"error":f"{id} is not a valid id {catagory}"}
    else:
        return {"error":f"{id} is not a valid id {catagory}"}
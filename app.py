from crypt import methods
from operator import contains
from flask import Flask, redirect, render_template, url_for, request, jsonify
from dynamicModel import db, Potion

#to see the result type "flask run" into the terminal

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = False
db.init_app(app)

'''
@app.route('/')#<-- called "Decorator"
def home():
    return 'You are now home'
'''

@app.route('/',methods['GET','POST'])
def home():
    return render_template('index.jinja', msg="testing", letters=['a','b','c'])

@app.route('/about')
def home():
    return render_template('home.jinja')

'''
@app.route('/inventory')
def inventory(): #<-- create a dictonary using JSON method/format (in postman use localhost5000:/inventory to access the dictionary)
    data = Potion.query.all()
    if 'list' not in type(data):
        potions = []
        for p in data:
            potions.append(p.to_dict())
        else:
            potions.append(data.to_dict())

    stock = {
        'potions' : potions
    }
    return stock

@app.route('/potions', methods=['POST'])
def create_potion():
    f_name = request.form['name']
    f_quantity = request.form['quantity']
    f_price = request.form['price']
    to_add = Potion(name=f_name, quantity=f_quantity, price=f_price)
    db.session.add(to_add)
    db.session.commit()
    return redirect(url_for('inventory'))

'''

'''
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
'''
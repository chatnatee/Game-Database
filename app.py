from flask import Flask, redirect, render_template, url_for, request, jsonify
from dynamicModel import db, Potion

#to see the result type "flask run" into the terminal

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

'''
@app.route('/')#<-- called "Decorator"
def home():
    return 'You are now home'
'''

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('page.html', title='home', message="Welcome home!")

@app.route('/about')
def about():
    return render_template('page.html', title='about', message="this is the about page lol.")


@app.route('/inventory')
def inventory():
    data = Potion.query.all()
    return render_template('inventory.html', title='Inventory', potions=data)

@app.route('/potion', methods=['GET','POST'])
def create_potion():
    if request.method == 'GET':
        return render_template('potion.html', title='Add a Potion')
    else:
        f_name = request.form['name']
        f_quantity = request.form['quantity']
        f_price = request.form['price']
        to_add = Potion(name=f_name, quantity=f_quantity, price=f_price)
        db.session.add(to_add)
        db.session.commit()
        return redirect(url_for('inventory'))

@app.route('/filter-items', methods=['GET','POST'])
def filter_items():
    if request.method == 'GET':
        return render_template('search.html', title='Search')
    else:
        f_max = request.form['max']
        data = Potion.query.filter(Potion.price <= int(f_max)).all()
        return render_template('inventory.html', title="Search results", potions=data)

'''
    else:
        f_max = request.form['max']
        data = Potion.query.filter(Potion.price.startswith("insert_name")).all()
        return render_template('inventory.html', title="Search results", potions=data)
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
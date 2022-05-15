from flask import Flask, redirect, render_template, url_for, request, jsonify
from dynamicModel import db, Games

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
    return render_template('page.html', title='home', message="Welcome homepage of video games database!")

@app.route('/about')
def about():
    return render_template('page.html', title='about', message="This database stores several video games informations (Name, Genre and Date of Release. Please the attached README.txt file for more instructions)")


@app.route('/all')
def all():
    data = Games.query.all()
    return render_template('all.html', title='All-Games', alls=data)

@app.route('/game', methods=['GET','POST'])
def create_games():
    if request.method == 'GET':
        return render_template('game.html', title='Add Games')
    else:
        f_name = request.form['name']
        f_genre = request.form['genre']
        f_dor = request.form['dor']
        to_add = Games(name=f_name, genre=f_genre, dor=f_dor)
        db.session.add(to_add)
        db.session.commit()
        return redirect(url_for('all'))

@app.route('/filter-games', methods=['GET','POST'])
def filter_games():
    if request.method == 'GET':
        return render_template('search.html', title='Search')
    else:
        f_numg = request.form['numg']
        data = Games.query.filter(Games.genre == int(f_numg)).all()
        return render_template('all.html', title="Search results", alls=data)

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
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
#welcome page
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('page.html', title='home', message="Welcome homepage of video games database!")

#about page
@app.route('/about')
def about():
    return render_template('page.html', title='about', message="This database stores several video games informations (Name, Genre and Date of Release. Please the attached README.txt file for more instructions)")

#all games listed in the database
@app.route('/all')
def all():
    data = Games.query.all()
    return render_template('all.html', title='All-Games', alls=data)

#puting in more games
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

#filter game by genre
@app.route('/filter-games', methods=['GET','POST'])
def filter_games():
    if request.method == 'GET':
        return render_template('search.html', title='Search')
    else:
        f_numg = request.form['genre']
        data = Games.query.filter(Games.genre == int(f_numg)).all()
        return render_template('all.html', title="Search results", alls=data)

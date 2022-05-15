from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    genre = db.Column(db.Integer, nullable=False)
    dor = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id}:{self.name}\tgenre:{self.genre}\tdor:{self.dor}'

    def to_dict(self):
        return {'id':self.id, 'name':self.name, 'genre':self.genre, 'dor':self.dor}


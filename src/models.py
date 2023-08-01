from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(150), unique = True, nullable = False)
    height = db.Column(db.String(150), unique = False, nullable = True)
    mass = db.Column(db.String(150), unique = False, nullable = True)
    hair_color = db.Column(db.String(150), unique = False, nullable = True)
    skin_color = db.Column(db.String(150), unique = False, nullable = True)
    eye_color = db.Column(db.String(150), unique = False, nullable = True)
    birth_year = db.Column(db.String(150), unique = False, nullable = True)
    gender = db.Column(db.String(150), unique = False, nullable = True)
    homeworld = db.Column(db.String(150), unique = False, nullable = True)

    def __repr__(self):
        return '<People %r' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld
        }

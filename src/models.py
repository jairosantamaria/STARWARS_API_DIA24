from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(String(250), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)

def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
       }
#nueva clase
class People(Base):
    __tablename__ = 'people'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    height = db.Column(Integer, nullable=False)
    mass = db.Column(Integer, nullable=False)
    hair_color = db.Column(String(250), nullable=False)
    skin_color = db.Column(String(250), nullable=False)
    birth_year = db.Column(Integer, nullable=False)
    gender = db.Column(String(250), nullable=False)
    home_world = db.Column(String(250), nullable=False)
    planet_id = db.Column(Integer, nullable=False)

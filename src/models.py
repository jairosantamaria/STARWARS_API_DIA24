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

class People(Base):
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

def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
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

class Starships(Base):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(250), nullable=False)
    model = db.Column(String(250), nullable=False)
    manufacturer = db.Column(String(250), nullable=False)
    cost_in_credits = db.Column(Integer, nullable=False)
    lenght = db.Column(Integer, nullable=False)
    max_atmospheric_speed = db.Column(Integer, nullable=False)
    crew = db.Column(String(250), nullable=False)
    passengers = db.Column(Integer, nullable=False)
    cargo_capacity = db.Column(Integer, nullable=False)
    consumables = db.Column(String(250), nullable=False)
    hyperdrive_rating = db.Column(Integer, nullable=False)
    MGLT = db.Column(Integer, nullable=False)
    starship_class = db.Column(String(250), nullable=False)
    pilots = db.Column(Integer, nullable=False)

def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorites(Base):
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('user.id'))
    people_id = db.Column(Integer, ForeignKey('people.id'))
    planet_id = db.Column(Integer, ForeignKey('planets.id'))
    starships_id = db.Column(Integer, ForeignKey('starships.id'))
   
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
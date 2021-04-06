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
            "nickname": self.nickname,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active,
        }

class People(db.Model):
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
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "home_world": self.home_world,
            "planet_id": self.planet_id,
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
        return '<Planet %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "description": self.description,
        }

class Starships(db.Model):
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
        return '<Starships %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "lenght": self.lenght,
            "max_atmospheric_speed": self.max_atmospheric_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "starship_class": self.starship_class,
            "pilots": self.pilots,
         }

#class Favorites(db.Model):
 #  user_id = db.Column(Integer, ForeignKey('user.id'))
 #   people_id = db.Column(Integer, ForeignKey('people.id'))
 #   planet_id = db.Column(Integer, ForeignKey('planet.id'))
 #   starships_id = db.Column(Integer, ForeignKey('starships.id'))
   
  #  def __repr__(self):
   #     return '<Favorites %r>' % self.username

  #  def serialize(self):
  #      return {
   #         "id": self.id,
  #          "email": self.email,
           
   #     }
"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planet, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#endpoint User____________________________________________________________________
@app.route('/user', methods=['GET'])
def get_user():
    
    users = User.query.all()
    all_user = list(map(lambda x: x.serialize(), users))
    return jsonify(all_user), 200

@app.route('/user/<int:id>', methods=['GET'])
def get_userid(id):
    userid = User.query.get(id)
    result = userid.serialize()
    return jsonify(result), 200

#endpoint People__________________________________________________________________
@app.route('/people', methods=['GET'])
def handle_people():
    
    peoplex = People.query.all()
    all_people = list(map(lambda x: x.serialize(), peoplex))
    return jsonify(all_peoplex), 200   

#endpoint Planet_________________________________________________________________
@app.route('/planet', methods=['GET'])
def handle_planet():

    planets = Planet.query.all()
    all_planet = list(map(lambda x: x.serialize(), planets))
    return jsonify(all_planets), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_planetid(id):
    planetid = User.query.get(id)
    result = planetid.serialize()
    return jsonify(result), 200

# this only runs if `$ python src/main.py` is executed __________________________
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

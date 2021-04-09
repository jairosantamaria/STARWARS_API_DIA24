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

#endpoint User
@app.route('/user', methods=['GET'])
def handle_hello():
    
    people_query = User.query.all()
    all_people = list(map(lambda x: x.serialize(), user_query))
    return jsonify(response_body), 200

 @app.route('/user', methods=['POST'])
 def handle_hello_post():
    
    request_body_user = request.get_json()
    user1 = User(nickname=request_body_user["nickname"], email=request_body_user["email"], password=request_body_user["password"])
    db.session.add(user1)
    db.session.commit()
    return jsonify(request_body_user), 200   

 @app.route('/user/<int:user_id>', methods=['DELETE'])
 def delete_user(user_id):
    user1 = User.query.get(user_id)
    if user1 is None:
        raise APIException('User not found', status_code=404)
    db.session.delet(user1)
    db.session.commit()
    return jsonify("Hecho"), 200

#endpoint People
@app.route('/people', methods=['GET'])
def handle_people():
    
    people_query = People.query.all()
    all_people = list(map(lambda x: x.serialize(), people_query))
    return jsonify(all_people), 200    

#endpoint Planet
@app.route('/planet', methods=['GET'])
def handle_planet():

    people_query = Planet.query.all()
    all_people = list(map(lambda x: x.serialize(), planet_query))
    return jsonify(response_body), 200

#endpoint Starships
@app.route('/starships', methods=['GET'])
def handle_starships():
    
    response_body = {
        "msg": "Hello, STARSHIPS this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

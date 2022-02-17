"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

jackson_family._members 

@app.route('/member/<member_id>', methods=['GET'])
def get_this_member(member_id):
    member = jackson_family.get_member(member_id)
    return jsonify(member), 200
    

@app.route('/member', methods=['POST'])
def add_new_member():
    member = request.get_json()
    sucess = jackson_family.add_member(member)
    if sucess == True:
        return jsonify('New member added'), 200
    else:
        return jsonify('Bad request'), 400

@app.route('/member/<member_id>', methods=['DELETE'])
def delete_this_member(member_id):
    return jsonify(jackson_family.delete_member(member_id)), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)
jackson_family = FamilyStructure("Medina")  # Create the jackson family object


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"hello": "world",
                     "family": members}
    return jsonify(response_body), 200


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    done = jackson_family.delete_member(member_id)
    if not done:
        response_body = {"message": "Integrante de la famimila es inexistente"}
        return response_body, 400
    response_body = {"done": True}
    return response_body, 200


@app.route('/member', methods=['POST'])
def add_member():
    request_body = request.json
    member = {"id": request_body.get("id") or jackson_family._generateId(),
              "first_name": request_body.get("first_name"),
              "age": request_body.get("age"),
              "lucky_numbers": request_body.get("lucky_numbers")}
    if not all(member.values()):
        response_body = {"message": "Faltan valores en su envío"}
        return response_body, 400
    response_body = jackson_family.add_member(member)
    return response_body, 200


@app.route('/member/<int:member_id>', methods=['GET'])
def get_one_member(member_id):
    result = jackson_family.get_member(member_id)
    if not result:
        response_body = {"message": "Integrante no encontrado"}
        return response_body, 400
    response_body = {"message": "Usuario encontrado",
                     "result": result[0]}
    return response_body, 200


# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

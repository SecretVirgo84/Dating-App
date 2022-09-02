from flask import Blueprint, jsonify, abort, request
from ..models import User, db
import hashlib
import secrets

def scramble(password, str):
    """Hash and salt the given password"""
    salt = secrets.token.hex(16)
    return hashlib.sha512((password + salt). encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix='/users')

#Get all users
@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all() # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response

#Get 1 user from the id specified
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    """ get 1 user from id """
    user = User.query.get_or_404(id)
    return jsonify(user.serialize())

#delete a specific user
@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
   
    user = User.query.get_or_404(id)  
    try:
        db.session.delete(user) # prepare DELETE statement
        db.session.commit()  
        return jsonify(True)
    except:
        # something went wrong
        return jsonify(False)


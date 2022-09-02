from flask import Blueprint, jsonify, abort, request
from ..models import Profile, db
import hashlib
import secrets

bp = Blueprint('profiles', __name__, url_prefix='/profiles')

#Get 1 proflie from the id specified
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    """ get 1 user profile """
    profile = profile.query.get_or_404(id)
    return jsonify(profile.serialize())
from flask import Blueprint, request
from ..models import User
from .. import db
from werkzeug.security import generate_password_hash
from ..auth import basic_auth_required
from ..decorators import self_access_required 

users_bp = Blueprint('users', __name__)

# POST /api/v1/users – Create new user
@users_bp.route('/', methods=['POST'])
@basic_auth_required
def register(user):
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return {"message": "Username and password are required."}, 401

    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return {"message": "This username is already taken."}, 401

    new_user = User(username=data['username'])
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return {"message": "Registration successful!"}, 201

# GET /api/v1/users/login – Login test
@users_bp.route('/login', methods=['GET'])
@basic_auth_required
def login(user):
    return {"message": f"Login successful. Welcome, {user.username}!"}

# GET /api/v1/users – Get all users
@users_bp.route('/', methods=['GET'])
@basic_auth_required
def get_all_users(user): 
    users = User.query.all()
    return [
        {"id": u.id, "username": u.username}
        for u in users
    ], 200

# GET /api/v1/users/<user_id> – Get specific user
@users_bp.route('/<int:user_id>', methods=['GET'])
@basic_auth_required
@self_access_required
def get_user_by_id(user, user_id):
    u = User.query.get(user_id)
    if not u:
        return {"message": "User not found."}, 404
    return {"id": u.id, "username": u.username}, 200

# PUT /api/v1/users/<user_id> – Update user info
@users_bp.route('/<int:user_id>', methods=['PUT'])
@basic_auth_required
@self_access_required
def update_user(user, user_id):
    data = request.get_json()
    if not data:
        return {"message": "No data provided."}, 400

    if data.get("username"):
        user.username = data["username"]
    if data.get("password"):
        user.set_password(data["password"])

    db.session.commit()
    return {
        "message": "User updated.",
        "user": {
            "id": user.id,
            "username": user.username
        }
    }, 200

# DELETE /api/v1/users/<user_id> – Delete user
@users_bp.route('/<int:user_id>', methods=['DELETE'])
@basic_auth_required
@self_access_required
def delete_user(user, user_id):
    db.session.delete(user)
    db.session.commit()
    return '', 204

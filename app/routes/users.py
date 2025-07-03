from flask import Blueprint, request
from ..models import User
from .. import db
from werkzeug.security import generate_password_hash
from ..auth import basic_auth_required

users_bp = Blueprint('users', __name__)

# POST /api/v1/users – Yeni kullanıcı oluştur
@users_bp.route('/', methods=['POST'])
@basic_auth_required
def register(user):
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return {"message": "Kullanıcı adı ve şifre gereklidir."}, 401

    # Aynı kullanıcı adı var mı?
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return {"message": "Bu kullanıcı adı zaten alınmış."}, 401

    # Yeni kullanıcıyı oluştur
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])

    db.session.add(new_user) # Veritabanına ekle
    db.session.commit()

    return {"message": "Kayıt başarılı!"}, 201

#  Kullanıcı giriş testi (kimlik kontrolü)
@users_bp.route('/login', methods=['GET'])
@basic_auth_required
def login(user):
    return {"message": f"Giriş başarılı, hoş geldin {user.username}!"}


# GET /api/v1/users – Tüm kullanıcıları getir
@users_bp.route('/', methods=['GET'])
@basic_auth_required
def get_all_users(user): 
    users = User.query.all()
    return [
        {"id": u.id, "username": u.username}
        for u in users
    ], 200

# GET /api/v1/users/<user_id> – Belirli bir kullanıcıyı getir
@users_bp.route('/<int:user_id>', methods=['GET'])
@basic_auth_required
def get_user_by_id(user, user_id):
    u = User.query.get(user_id)
    if not u:
        return {"message": "Kullanıcı bulunamadı."}, 404
    return {"id": u.id, "username": u.username}, 200

# PUT /api/v1/users/<user_id> – Kullanıcı bilgilerini güncelle
@users_bp.route('/<int:user_id>', methods=['PUT'])
@basic_auth_required
def update_user(user, user_id):
    if user.id != user_id:
        return {"message": "Sadece kendi hesabınızı güncelleyebilirsiniz."}, 403

    data = request.get_json()
    if not data:
        return {"message": "Veri bulunamadı."}, 400

    if data.get("username"):
        user.username = data["username"]
    if data.get("password"):
        user.set_password(data["password"])

    db.session.commit()
    return {"message": "Kullanıcı güncellendi.", "user": {
        "id": user.id,
        "username": user.username
    }}, 200

# DELETE /api/v1/users/<user_id> – Kullanıcıyı sil
@users_bp.route('/<int:user_id>', methods=['DELETE'])
@basic_auth_required
def delete_user(user, user_id):
    if user.id != user_id:
        return {"message": "Sadece kendi hesabınızı silebilirsiniz."}, 403

    db.session.delete(user)
    db.session.commit()
    return '', 204  # 204 No Content





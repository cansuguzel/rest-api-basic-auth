from . import db
from werkzeug.security import generate_password_hash, check_password_hash

# user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # storing password securely
    def set_password(self, password):
        self.password_hash = generate_password_hash(password) #password hashing

    # controlling password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# note model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

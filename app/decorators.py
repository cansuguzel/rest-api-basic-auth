from functools import wraps
from flask import jsonify, request

from app.models import Note

def self_access_required(f):
    @wraps(f)
    def decorated_function(user, user_id, *args, **kwargs):
        if user.id != user_id:
            return {"message": "You can only access your own account."}, 403
        return f(user, user_id, *args, **kwargs)
    return decorated_function

def owner_required(f):
    @wraps(f)
    def decorated_function(user, note_id, *args, **kwargs):
        note = Note.query.filter_by(id=note_id, user_id=user.id).first()
        if not note:
            return jsonify({"message": "Access denied: not your note."}), 403
        request.note = note
        return f(user, note_id, *args, **kwargs)
    return decorated_function

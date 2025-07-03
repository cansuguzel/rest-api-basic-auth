from flask import Blueprint, request
from ..models import Note
from .. import db
from ..auth import basic_auth_required #Bu fonksiyonla işaretlenmiş route’lara sadece doğru kullanıcı bilgisi ile erişilebilir.

notes_bp = Blueprint('notes', __name__)

# GET /api/v1/notes tüm notları listele (giriş yapan kullanıcıya ait olanları)
@notes_bp.route('/', methods=['GET'])
@basic_auth_required
def get_notes(user):
    notes = Note.query.filter_by(user_id=user.id).all()
    return [
        {"id": note.id, "title": note.title, "content": note.content}
        for note in notes
    ]

# POST /api/v1/notes Yeni not ekliyor
@notes_bp.route('/', methods=['POST'])
@basic_auth_required
def add_note(user):
    data = request.get_json()

    if not data or not data.get("title"):
        return {"message": "Başlık alanı gereklidir."}, 400

    new_note = Note(
        title=data["title"],
        content=data.get("content", ""),
        user_id=user.id
    )

    db.session.add(new_note)
    db.session.commit() # değişiklik veritabanına kaydedilir.

    return {"message": "Not eklendi.", "note_id": new_note.id}, 201

#GET /api/v1/notes/<id> — Tek notu ID ile getir
@notes_bp.route('/<int:note_id>', methods=['GET'])
@basic_auth_required
def get_note_by_id(user, note_id):
    note = Note.query.filter_by(id=note_id, user_id=user.id).first()
    if not note:
        return {"message": "Not bulunamadı."}, 404

    return {"id": note.id, "title": note.title, "content": note.content}, 200

# PUT /api/v1/notes/<id> — Notu güncelle
@notes_bp.route('/<int:note_id>', methods=['PUT'])
@basic_auth_required
def update_note(user, note_id):
    note = Note.query.filter_by(id=note_id, user_id=user.id).first()
    if not note:
        return {"message": "Not bulunamadı."}, 404

    data = request.get_json()
    if not data:
        return {"message": "Veri alınamadı."}, 400

    note.title = data.get("title", note.title)
    note.content = data.get("content", note.content)

    db.session.commit()

    return {"message": "Not güncellendi.", "note": {
        "id": note.id,
        "title": note.title,
        "content": note.content
    }}, 200


# DELETE /api/v1/notes/<id> notu sil
@notes_bp.route('/<int:note_id>', methods=['DELETE'])
@basic_auth_required
def delete_note(user, note_id):
    note = Note.query.filter_by(id=note_id, user_id=user.id).first()

    if not note:
        return {"message": "Not bulunamadı."}, 404

    db.session.delete(note)
    db.session.commit() 
    return '', 204

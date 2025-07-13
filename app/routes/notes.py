from flask import Blueprint, request
from ..models import Note
from .. import db
from ..auth import basic_auth_required
from ..decorators import owner_required 

notes_bp = Blueprint('notes', __name__)

# GET /api/v1/notes – List all notes for the authenticated user
@notes_bp.route('/', methods=['GET'])
@basic_auth_required
def get_notes(user):
    notes = Note.query.filter_by(user_id=user.id).all()
    return [
        {"id": note.id, "title": note.title, "content": note.content}
        for note in notes
    ]

# POST /api/v1/notes – Create a new note
@notes_bp.route('/', methods=['POST'])
@basic_auth_required
def add_note(user):
    data = request.get_json()

    if not data or not data.get("title") or not data.get("content"):
        return {"message": "Title and content are required."}, 400

    new_note = Note(
        title=data["title"],
        content=data.get("content", ""),
        user_id=user.id
    )

    db.session.add(new_note)
    db.session.commit()

    return {"message": "Note created.", "note_id": new_note.id}, 201

# GET /api/v1/notes/<id> – Get note by ID
@notes_bp.route('/<int:note_id>', methods=['GET'])
@basic_auth_required
@owner_required
def get_note_by_id(user, note_id):
    note = request.note
    return {"id": note.id, "title": note.title, "content": note.content}, 200

# PUT /api/v1/notes/<id> – Update a note
@notes_bp.route('/<int:note_id>', methods=['PUT'])
@basic_auth_required
@owner_required
def update_note(user, note_id):
    note = request.note
    data = request.get_json()
    if not data or not data.get("title") or not data.get("content"):
        return {"message": "Title and content are required."}, 400

    note.title = data.get("title", note.title)
    note.content = data.get("content", note.content)

    db.session.commit()

    return {
        "message": "Note updated.",
        "note": {
            "id": note.id,
            "title": note.title,
            "content": note.content
        }
    }, 200

# DELETE /api/v1/notes/<id> – Delete a note
@notes_bp.route('/<int:note_id>', methods=['DELETE'])
@basic_auth_required
@owner_required
def delete_note(user, note_id):
    note = request.note

    db.session.delete(note)
    db.session.commit()
    return '', 204

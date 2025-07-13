from app import create_app, db
from app.models import User, Note

app = create_app()

with app.app_context():
    db.create_all()
    print("database created and tables added.")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # database configuration taken from config
    app.config.from_object('config.Config')

    # initialize the database
    db.init_app(app)

    # add routes
    from .routes.notes import notes_bp
    from .routes.users import users_bp
    
    # register blueprints
    app.register_blueprint(notes_bp, url_prefix='/api/v1/notes')
    app.register_blueprint(users_bp, url_prefix='/api/v1/users')

    return app
# This function creates and configures the Flask application.
# It initializes the database and registers the blueprints for notes and users routes.  
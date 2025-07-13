from flask import request
from functools import wraps
from .models import User
from . import db # db  SQLAlchemy is the database object.

#  decorator for basic authentication
def basic_auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization #it retrieves the HTTP Basic Auth credentials from the request.
        # 1. if the username or password is missing
        if not auth or not auth.username or not auth.password:
            return {"message": "Authentication required."}, 401

        # 2. Look up the user in the database
        user = User.query.filter_by(username=auth.username).first()

        # 3. If the user is not found or the password is incorrect
        if not user or not user.check_password(auth.password):
            return {"message": "Invalid username or password."}, 401

        # 4. If everything is correct, proceed to the function
        return f(user, *args, **kwargs)

    return decorated_function


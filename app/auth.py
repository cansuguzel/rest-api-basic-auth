from flask import request
from functools import wraps
from .models import User
from . import db # db  SQLAlchemy veritabanı nesnesi.

#  Auth işlemi için decorator
def basic_auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization #HTTP isteğindeki username ve password bilgisini alır

        # 1. Kullanıcı adı ve şifre yoksa
        if not auth or not auth.username or not auth.password:
            return {"message": "Kimlik doğrulama gerekli."}, 401

        # 2. Kullanıcıyı veritabanında ara
        user = User.query.filter_by(username=auth.username).first()

        # 3. Kullanıcı bulunamadıysa veya şifre yanlışsa
        if not user or not user.check_password(auth.password):
            return {"message": "Geçersiz kullanıcı adı veya şifre."}, 401

        # 4. Her şey doğruysa, fonksiyona devam et
        return f(user, *args, **kwargs)

    return decorated_function


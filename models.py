from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    NAME = db.Column(db.String(50), primary_key = True)
    BIRTHDAY = db.Column(db.String(50))
    EMAIL = db.Column(db.String(200), nullable = False, unique = True)
    PASSWORD = db.Column(db.String(200), nullable = False)
    GENDER = db.Column(db.String(50), nullable = False)

    def __init__(self, name, email, password, gender):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.gender = gender

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
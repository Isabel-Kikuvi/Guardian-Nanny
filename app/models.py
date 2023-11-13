from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
from app import db
from time import time
import jwt
from app import app

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# User models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    selected_nannies = db.relationship('NannySelection', back_populates='user')
    about_me = db.Column(db.String(140))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
        
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
    
# Nanny Model
class Nanny(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
 
    selected_by_users = db.relationship('NannySelection', back_populates='nanny')

# NannySelection Model (Many-to-Many Relationship)
class NannySelection(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    nanny_id = db.Column(db.Integer, db.ForeignKey('nanny.id'), primary_key=True)
    
    user = db.relationship('User', back_populates='selected_nannies')
    nanny = db.relationship('Nanny', back_populates='selected_by_users')
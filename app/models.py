from app import db

# User models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    selected_nannies = db.relationship('NannySelection', back_populates='user')

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
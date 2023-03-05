from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin): #Creating user table
    id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    username =db.Column(db.String(80))
    links = db.relationship('Link')
    
class Link(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'))
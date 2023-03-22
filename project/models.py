from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin): #Creating user table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    links = db.relationship('Link')
    
    def __repr__(self):
        return '<Username %r>' % self.username
    
    
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50))
    
    def __repr__(self):
        return '<Name %r>' % self.name
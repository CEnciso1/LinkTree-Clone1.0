from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ, path
from sqlalchemy import create_engine
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

engine = create_engine(environ.get('SQLALCHEMY_DATABASE_URI'))
connection = engine.connect()
db = SQLAlchemy()
DB_NAME = 'test.db'

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    from .models import User, Link
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('project/' + DB_NAME):
        db.create_all(app=app)
        print("Database Created")

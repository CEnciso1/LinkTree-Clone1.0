from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ, path
from dotenv import load_dotenv
from flask_login import LoginManager

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_pyfile('config.py')     #Configures application with contents of config.py
    db.init_app(app)                        #Link database to app
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Link  #Ensures model classes are defined
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))   
    
    return app

def create_database(app):
    #if not path.exists('project/'+ 'database.d'):
    with app.app_context():
        db.create_all()
        print('Database Created')
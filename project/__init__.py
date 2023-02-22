from flask import Flask
from flask_mysqldb import MySQL

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_pyfile('config.py')

    mysql = MySQL(app)
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app

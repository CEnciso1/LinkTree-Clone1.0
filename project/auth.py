from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if password1 != password2:
            flash('Passwords don\'t match', category='error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password1,'sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account has been created!')
            return redirect(url_for('views.home'))
    return render_template('signup.html')
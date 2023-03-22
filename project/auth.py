from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash('You Are Logged In', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password try again', category='error')
        else:
            flash('No account with that email exists', category='error')
    return render_template('login.html', user=current_user)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.landing'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email = email).first()
        if password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif user:
            flash('A an account with this email already exists', category='error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password1,'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account has been created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('signup.html', user=current_user)
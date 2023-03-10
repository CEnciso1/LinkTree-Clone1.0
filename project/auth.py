from flask import Blueprint, render_template, request, flash

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
        emailUsername = request.form.get('email-username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if password1 != password2:
            flash('Passwords don\'t match', category='error')
        else:
            pass
        
    return render_template('signup.html')
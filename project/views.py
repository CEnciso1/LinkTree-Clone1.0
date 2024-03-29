from flask import Blueprint, render_template
from flask_login import login_required, current_user
views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html', user=current_user) # allows use of user attributes in template

@views.route('/', methods=['GET', 'POST'])
def landing():
    return render_template('landing.html', user=current_user)
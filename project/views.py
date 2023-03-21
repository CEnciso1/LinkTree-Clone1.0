from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@views.route('/', methods=['GET', 'POST'])
def landing():
    return render_template('landing.html')
from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hi_nubila():
    return 'Hi! nubila'

@bp.route('/home')
def nubila():
    return render_template('home.html')
from flask import (
    Blueprint, request, render_template, flash, g, session,
    redirect, url_for
)

bp_home = Blueprint('home', __name__)

@bp_home.route('/')
def index():
    return render_template('home/index.html')

@bp_home.route('/about')
def about():
    return render_template('home/about.html')

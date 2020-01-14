from flask import (
    Blueprint, request, render_template, flash, g, session,
    redirect, url_for
)
from flask_login import login_user, current_user, logout_user, login_required

from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.auth.forms import LoginForm, RegForm
from app.auth.models import User

bp_auth = Blueprint('auth', __name__)

@bp_auth.route('/')
def home(user=None):
    return render_template('auth/index.html')


@bp_auth.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            # if not is_safe_url(next_page):
            #     return flask.abort(400)
            flash('Logged in successfully!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home.index'))
        else:
            flash('Incorrect email or password', 'warning')
    else:
        return render_template('auth/login.html', form=form)


@bp_auth.route('/logout')
def logout():
    flash('Successfully logged out', 'success')
    logout_user()
    return redirect(url_for('home.index'))


@bp_auth.route('/register', methods=('GET', 'POST'))
def register():
    form = RegForm()
    if form.validate_on_submit():
        error = False
        user_name = User.query.filter_by(name=form.name.data).first()
        user_email = User.query.filter_by(email=form.email.data).first()
        if user_name:
            error = True
            flash(f'User name {user_name.name} is already used. Choose a different one', 'warning')
        if user_email:
            error = True
            flash(f'Email {user_email.email} is already used. Choose a different one', 'warning')
        if not error:
            name = form.name.data
            email = email=form.email.data
            password = generate_password_hash(form.password.data)
            user = User(name=name, email=email, password=password, role=1, status=1)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('auth.login'))
    return render_template('/auth/register.html', form=form)


@bp_auth.route('/profile')
@login_required
def profile():
    if current_user:
        return render_template('/auth/profile.html')
    else:
        return redirect(url_for('home.index'))



from flask import (
    Blueprint, request, render_template, flash, g, session,
    redirect, url_for
)
from flask_login import login_user, current_user, logout_user, login_required

from app import db
from app.auth.forms import LoginForm, RegForm
from app.auth.models import User

bp_admin = Blueprint('admin', __name__)

@bp_admin.route('/')
@login_required
def home(user=None):
    return render_template('admin/index.html')
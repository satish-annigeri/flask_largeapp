from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


from app.home.controllers import bp_home
app.register_blueprint(bp_home)

from app.auth.controllers import bp_auth
app.register_blueprint(bp_auth, url_prefix='/auth')

from app.admin.controllers import bp_admin
app.register_blueprint(bp_admin, url_prefix='/admin')
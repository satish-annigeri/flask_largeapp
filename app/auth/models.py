from app import db, login_manager
from flask_login import UserMixin

class Base(db.Model, UserMixin):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(Base):
    __tablename__ = 'auth_user'

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    def __init__(self, name, email, password, role, status):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.status = status

    def __repr__(self):
        return f"User: {self.name} {self.email} role: {self.role} status: {self.status}"


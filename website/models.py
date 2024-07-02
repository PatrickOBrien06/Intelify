from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String, unique=True, nullable=False)
  username = db.Column(db.String, nullable=False)
  password = db.Column(db.String, nullable=False)
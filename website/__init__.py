from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import SECRET_KEY

login_manager = LoginManager()

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = SECRET_KEY
  app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
  app.config['SESSION_PERMANENT'] = True
  app.config['PERMANENT_SESSION_LIFETIME'] = 604800
  # app.config['SESSION_COOKIE_SECURE'] = True
  db.init_app(app)

  from .auth import auth
  app.register_blueprint(auth)

  from .ai import ai
  app.register_blueprint(ai)

  from .models import User

  create_database(app)

  login_manager.login_view = "auth.login"
  login_manager.login_message = "You must be signed in to reach this page!"
  login_manager.login_message_category = "danger"
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))
  
  return app

def create_database(app):
  with app.app_context():
    db.create_all()
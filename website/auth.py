from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db


auth = Blueprint('auth', __name__, template_folder="templates")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
  if request.method == "POST":

    username = request.form.get("username")
    email = request.form.get("email")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

    email_exists = User.query.filter_by(email=email).first()

    if email_exists:
      flash("Email already exists!", "danger")

    elif password1 != password2:
      flash("Passwords do not match!", "danger")

    else:
      password_hash = generate_password_hash(password1, method='pbkdf2')
      user = User(username=username, email=email, password=password_hash)
      db.session.add(user)
      db.session.commit()
      login_user(user, remember=True)
      flash("Account created!", "success")
      return redirect(url_for("ai.home"))
   

  return render_template("signup.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:
      if check_password_hash(user.password, password):
        login_user(user, remember=True)
        flash("Logged In!", "success")
        return redirect(url_for("ai.home"))
      else:
        flash("Invalid Email or Password", "danger")
    else:
      flash("Invalid Email or Password", "danger")

  return render_template("login.html")
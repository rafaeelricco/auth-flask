from datetime import timedelta

from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app.factory import bcrypt, db
from app.models.model import User


# Route to register a new user
@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=bcrypt.generate_password_hash(form.password.data).decode("utf-8"),
        )
        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        except:
            return print("Erro ao criar usuário")
    return render_template("register.html", form=form)


# Route to login a user
@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            login_remembered = request.form.get("remember")

            if login_remembered:
                login_user(user, remember=True, duration=timedelta(days=7))
            elif not login_remembered:
                login_user(user, remember=False)
                return (
                    redirect(next_page)
                    if next_page
                    else redirect(url_for("home.index"))
                )

            else:
                flash(
                    "Login inválido. Por favor, verifique seu usuário e senha.",
                    "danger",
                )
                return render_template("login.html", form=form)

    return render_template("login.html", form=form)


# Route to logout
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.index"))

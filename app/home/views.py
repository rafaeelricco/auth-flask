from flask import render_template
from flask_login import current_user, login_required

from app.factory import login_manager
from app.home import home
from app.models.model import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@home.route("/")
@login_required
def index():
    user = User.query.filter_by(id=current_user.id).first()
    return render_template("index.html", user=user)


@home.route("/profile")
@login_required
def profile():
    user = User.query.filter_by(id=current_user.id).first()
    return render_template("profile.html", user=user)

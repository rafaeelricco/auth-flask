from flask_login import UserMixin

from app.factory import db


# Table of users
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

    def get_id(self):
        return self.id

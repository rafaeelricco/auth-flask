from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    PasswordField,
    StringField,
    SubmitField,
    ValidationError,
)
from wtforms.validators import InputRequired, Length, Regexp

from app.models.model import User


class RegisterForm(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(min=4, max=25),
            Regexp(
                "^[A-Za-z0-9_]{3,}$",
            ),
        ],
    )
    password = PasswordField(
        validators=[
            InputRequired(),
            Length(min=6, max=40),
            Regexp(
                r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$",
            ),
        ],
    )
    submit = SubmitField("Criar conta")

    # Check if username already exists
    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Este nome de usuário já existe.")
        else:
            return username


class LoginForm(FlaskForm):
    username = StringField(
        validators=[InputRequired(), Length(1, 64)],
        render_kw={"placeholder": "Nome de usuário"},
    )
    password = PasswordField(
        validators=[
            InputRequired(),
            Length(1, 64),
            Regexp(
                r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$",
            ),
        ],
        render_kw={"placeholder": "Senha"},
    )
    remember = BooleanField("Remember me")
    submit = SubmitField("Entrar")

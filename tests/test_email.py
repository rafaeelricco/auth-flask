import os
from tests.fixtures import app
from tests.test_auth import user_test_data
from itsdangerous import URLSafeTimedSerializer
from app.models.base import User
from flask import make_response, jsonify

secret_key = URLSafeTimedSerializer(os.getenv("SECRET_KEY"))


def test_send_email(client):
    """User test to send email"""
    user = {
        "username": user_test_data["username"],
        "email": user_test_data["email"],
    }

    """ in route /send-email the token is generated using the email and the salt """
    response = client.post("/auth/register", json=user)

    """ if the email is sent, the user is redirected to the login page """
    if response.status_code == 200:
        return print("Email sent")
    else:
        return print("Email not sent, maybe the email is already registered")


def test_token_confirmation(client):
    """User test to confirm email"""
    user = {
        "username": user_test_data["username"],
        "email": user_test_data["email"],
    }

    """ in route /confirm/<token> the token is generated using the email and the salt """
    token = secret_key.dumps(user["email"], salt="email-confirm")

    """ the token is passed as a parameter in the route """
    response = client.get(f"/confirm/{token}")

    """ if the token is valid, the user is redirected to the login page """
    if response.status_code == 200:
        return print("Email confirmed")
    else:
        return print(
            "Email not confirmed, maybe the token is invalid or you are already confirmed"
        )


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


def test_load_user(client):
    """User test to load user"""
    user = {
        "username": user_test_data["username"],
        "email": user_test_data["email"],
    }

    """ Run query to get user """
    user = User.query.filter_by(email=user["email"]).first_or_404()

    """ Check if the user is loaded """
    if user:
        return print("User loaded")
    else:
        return print("User not loaded")

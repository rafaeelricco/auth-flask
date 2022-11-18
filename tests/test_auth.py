from tests.fixtures import app


user_test_data = {
    "username": "user test",
    "email": "usertest@gmail.com",
    "password": "password",
}


def test_register(app):
    """Test that a user can register"""
    with app.test_client() as client:
        response = client.post(
            "/auth/register",
            json=user_test_data,
        )
        assert response.status_code == 200 or 201


def test_login(app):
    """Test that a user can login"""
    with app.test_client() as client:
        response = client.post(
            "/auth/login",
            json=user_test_data,
        )
    assert response.status_code == 200 or 201


def test_logout(app):
    """Test that a user can logout"""
    with app.test_client() as client:
        response = client.post(
            "/auth/logout",
            json=user_test_data,
        )
    assert response.status_code == 200 or 201


def test_wrong_login(app):
    """Test that a user can't login with wrong credentials"""
    with app.test_client() as client:
        response = client.post(
            "/auth/login",
            json={
                "username": "wrong user",
                "email": "wrong email",
                "password": "wrong password",
            },
        )
    assert response.status_code == 404


def test_wrong_register(app):
    """Test that a user can't register with wrong credentials"""
    with app.test_client() as client:
        response = client.post(
            "/auth/register",
            json={
                "username": "wrong user",
                "email": "wrong email",
                "password": "wrong password",
            },
        )
    assert response.status_code == 400 or 404

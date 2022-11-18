from pytest import fixture
from app.factory import create_app, db


@fixture
def app():
    """Create and configure a new app instance for each test"""
    app = create_app("testing")
    """ Creating database in memory """
    with app.app_context():
        db.create_all()
    yield app

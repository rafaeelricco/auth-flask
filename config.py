import os

from decouple import config

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def create_sqlite_uri(database):
    return f"sqlite:///{os.path.join(BASEDIR, database)}"


class Config:
    SECRET_KEY = config("SECRET_KEY")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("development.db")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("testing.db")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("production.db")


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}

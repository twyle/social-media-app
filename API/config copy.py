"""
Empty module docstring
"""
import os


class BaseConfig():
    """
    Empty class docstring
    """

    SECRET_KEY = 'SECRET_KEY'
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    MONGODB_CONNECT = True

class TestingConfig(BaseConfig):
    """Empty class docstring"""

    DEBUG = True
    TESTING = True

    MONGODB_DB = os.environ['MONGODB_DB_TEST']
    MONGODB_HOST = os.environ['MONGODB_HOST_TEST']
    MONGODB_PORT = os.environ['MONGODB_PORT_TEST']
    MONGODB_USERNAME = os.environ['MONGODB_USERNAME_TEST']
    MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD_TEST']


class DevelopmentConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = True
    TESTING = False

    MONGODB_DB = os.environ['MONGODB_DB_DEV']
    MONGODB_HOST = os.environ['MONGODB_HOST_DEV']
    MONGODB_PORT = os.environ['MONGODB_PORT_DEV']
    MONGODB_USERNAME = os.environ['MONGODB_USERNAME_DEV']
    MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD_DEV']


class ProductionConfig(BaseConfig):
    """
    Empty class docstring
    """

    DEBUG = False
    TESTING = False

    MONGODB_DB = os.environ['MONGODB_DB_PROD']
    MONGODB_HOST = os.environ['MONGODB_HOST_PROD']
    MONGODB_PORT = os.environ['MONGODB_PORT_PROD']
    MONGODB_USERNAME = os.environ['MONGODB_USERNAME_PROD']
    MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD_PROD']

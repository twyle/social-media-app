"""
Empty module docstring
"""
import os

from flask import Flask
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)

def set_flask_environment() -> str:
    """Sets the flask development environment

    Raises
    ------
    KeyError
        If the FLASK_ENV environment variable is not set.

    Returns
    -------
    str:
        Flask operating environment i.e development 
    """

    if os.environ['FLASK_ENV'] == 'production':  # pragma: no cover
        app.config.from_object('API.config.ProductionConfig')
    elif os.environ['FLASK_ENV'] == 'development':  # pragma: no cover
        app.config.from_object('API.config.DevelopmentConfig')
    elif os.environ['FLASK_ENV'] == 'test':
        app.config.from_object('API.config.TestingConfig')

    return os.environ['FLASK_ENV']


set_flask_environment()

from API import routes
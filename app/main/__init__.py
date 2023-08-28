from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restx import Api
from flask import Blueprint

api_v1 = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    api_v1,
    version="1.0",
    title="Product API",
    description="A simple PRODUCT API",
)

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    app.register_blueprint(api_v1)

    return app

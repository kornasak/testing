from flask import Flask
from flask_bcrypt import Bcrypt
from .config import Config
from flask_cors import CORS


flask_bcrypt = Bcrypt()

def create_app():
    app = Flask(Config.FLASK_APP)
    app.config.from_object(Config)
    flask_bcrypt.init_app(app)
    CORS(app)
    return app
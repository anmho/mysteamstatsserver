from flask import Flask
from .api import api
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile("config.py")
    app.register_blueprint(api, url_prefix="/api")

    # Bind packages to Flask app
    cors = CORS()
    cors.init_app(app=app, origins=["*"])
    return app

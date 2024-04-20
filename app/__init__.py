import secrets

from flask import Flask
from flask_cors import CORS

from app.blueprints import auth, index, trees

__secret_key = secrets.token_hex()


def create_app():
    app = Flask(
        __name__,
        static_folder="../plantmi-frontend/dist",
        static_url_path="",
    )
    CORS(app)

    app.secret_key = __secret_key

    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(trees.bp)

    return app

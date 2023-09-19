from flask import Flask

from app.blueprints import auth, index

__secret_key = "6b23798833b26e1ea779b921982cacc236fb139c5e5ff0a26a394c2163031aad"


def create_app():
    app = Flask(__name__)

    app.secret_key = __secret_key

    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)

    return app

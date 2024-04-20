from flask import Blueprint

bp = Blueprint("index", __name__, url_prefix="/")
bp.static_folder = "../../plantmi-frontend/dist"


@bp.route("/", methods=("GET",))
def index():
    return bp.send_static_file("index.html")

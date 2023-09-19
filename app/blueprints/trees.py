from flask import Blueprint

bp = Blueprint("trees", __name__, url_prefix="/trees")


@bp.get("/")
def get_trees():
    return {
        "trees": [
            {
                "xpos": 12.0,
                "ypos": 15.0,
                "status": "no_status",
                "donation_status": {},
            }
        ]
    }

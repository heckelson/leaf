from db import add_vote_for_user, fetch_all_trees_from_db, fetch_all_votes_for_user
from flask import Blueprint, session

bp = Blueprint("trees", __name__, url_prefix="/trees")


@bp.get("/")
def get_trees():
    return fetch_all_trees_from_db()


@bp.get("/votes")
def get_votes():
    if "username" not in session:
        return {"error": "Not authenticated"}, 400

    return fetch_all_votes_for_user(session["username"])


@bp.post("/vote/<int:tree_id>")
def add_new_vote(tree_id: int):
    if "username" not in session:
        return {"error": "Not authenticated"}, 400

    add_vote_for_user(session["username"], tree_id)

    return {"ok": 1}, 200

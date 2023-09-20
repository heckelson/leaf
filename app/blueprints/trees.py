from flask import Blueprint, flash, redirect, request, session, url_for

from app.db import (
    add_user_donation,
    add_vote_for_user,
    fetch_all_trees_from_db,
    fetch_all_votes_for_user,
)

bp = Blueprint("trees", __name__, url_prefix="/trees")


@bp.get("/")
def get_trees():
    return fetch_all_trees_from_db()


@bp.get("/votes")
def get_votes():
    if "username" not in session:
        return {"error": "Not authenticated"}, 401

    return fetch_all_votes_for_user(session["username"])


@bp.post("/vote")
def add_new_vote():
    if "username" not in session:
        return {"error": "Not authenticated"}, 401

    if not ("tree_id" in request.json):
        return {"error": "Malformed request"}, 400

    try:
        tree_id = int(request.json["tree_id"])
    except ValueError:
        return {"error": "Malformed request"}, 400

    add_vote_for_user(session.get("username"), tree_id)

    return redirect(url_for("index.index"))


@bp.post("/fund")
def fund_tree():
    if "username" not in session:
        return {"error": "Not authenticated"}, 401

    if not ("tree_id" in request.form and "amount" in request.form):
        return {"error": "Malformed request"}, 400

    try:
        tree_id = int(request.form["tree_id"])
        amount = float(request.form["amount"])
    except ValueError:
        return {"error": "Malformed request"}, 400

    add_user_donation(session.get("username"), tree_id, amount)

    flash(f"Thank you for donating €{amount} to Tree #{tree_id+1}!")

    return redirect(url_for("index.index"))

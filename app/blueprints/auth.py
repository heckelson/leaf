from flask import Blueprint, flash, redirect, request, session, url_for

from app.crypt import password_matches
from app.db import fetch_user_from_db
from app.flash_categories import FlashCategory as FC

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/logout", methods=("GET", "POST"))
def logout():
    if "username" in session:
        session.pop("username")
        flash("Logged out", FC.SUCCESS)

    resp = redirect(url_for("index.index"))
    resp.delete_cookie("username")

    return resp


@bp.post("/login")
def login():
    if (
        not hasattr(request, "form")
        or "username" not in request.form
        or not request.form["username"]
    ):
        flash("No Username provided!", FC.ERROR)
        return redirect(url_for("index.index"))

    if (
        not hasattr(request, "form")
        or "password" not in request.form
        or not request.form["password"]
    ):
        flash("No password provided!", FC.ERROR)
        return redirect(url_for("index.index"))

    provided_username = request.form["username"]
    provided_password = request.form["password"]

    if (user := fetch_user_from_db(provided_username)) is not None and password_matches(
        provided_password, user.password_salt, user.password_hash
    ):
        session["username"] = user.username
    else:
        flash("Wrong username or password!", FC.ERROR)

    resp = redirect(url_for("index.index"))
    resp.set_cookie("username", provided_username)

    return resp

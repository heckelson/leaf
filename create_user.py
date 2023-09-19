#!/usr/bin/env python

from sqlalchemy.orm import Session

from app.crypt import *
from app.db import Role, User, get_engine

while True:
    username = input("What is your username going to be? >> ")
    password = input("What is your password going to be? >> ")

    while True:
        role = input("What is the user's role? Normal user (0), Admin(1) >> ")

        match role:
            case "0":
                role = Role.NORMAL_USER
                break
            case "1":
                role = Role.ADMIN
                break
            case _:
                print("Invalid role. Let's try again!")

    works_for_you = input("Is this information correct? [y/N]")
    if works_for_you.lower() == "y":
        break
    print("Let's try this again then...")

engine = get_engine()
password_salt = generate_salt()
password_hash = hash_password(password, password_salt)

with Session(engine) as session:
    user = User(
        username=username,
        role=role,
        password_hash=password_hash,
        password_salt=password_salt,
    )

    session.add(user)

    session.commit()
    print("All done.")

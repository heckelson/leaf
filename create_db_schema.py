#!/usr/bin/env python

if __name__ == "__main__":
    import os

    from app.db import Base, get_engine

    if (
        input("Are you sure you wanna recreate the database schema [y/N]? >> ").lower()
        != "y"
    ):
        exit(0)

    DB_FILE = "./test.db"

    if os.path.isfile(DB_FILE):
        os.remove(DB_FILE)

    engine = get_engine(echo=False)
    Base.metadata.create_all(engine)

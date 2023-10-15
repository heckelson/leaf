#!/usr/bin/env python

if __name__ == "__main__":
    import os

    import argparse

    from app.db import Base, get_engine

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-y",
        "--no-confirm",
        action="store_true",
        help="Do this without confirmation.",
    )

    args = parser.parse_args()

    # fmt: off
    if (
        not args.no_confirm
        and input("Are you sure you wanna recreate the database schema [y/N]? >> ").lower()
        != "y"
    ):
        # fmt: on
        exit(0)

    DB_FILE = "./test.db"

    if os.path.isfile(DB_FILE):
        os.remove(DB_FILE)

    engine = get_engine(echo=False)
    Base.metadata.create_all(engine)

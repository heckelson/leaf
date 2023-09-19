from pprint import pprint

from app.db import fetch_all_trees_from_db

if __name__ == "__main__":
    pprint(fetch_all_trees_from_db())

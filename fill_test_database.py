if __name__ == "__main__":
    import random
    from crypt import generate_salt, hash_password
    from random import sample

    from db import Donation, Role, Tree, TreeStatus, User, Vote, get_engine
    from generators import generate_username
    from sqlalchemy.orm import Session

    def user_gen():
        test_user_password = "12345"
        test_user_salt = generate_salt()
        test_user_password_hash = hash_password(test_user_password, test_user_salt)

        user = User(
            username=generate_username(),
            password_hash=test_user_password_hash,
            password_salt=test_user_salt,
            role=Role.NORMAL_USER,
        )

        yield user

    engine = get_engine()

    users = [next(user_gen()) for _ in range(10)]
    trees = [
        Tree(id=0, xpos=48.208119, ypos=16.371828, status=TreeStatus.DONE),
        Tree(id=1, xpos=48.208991, ypos=16.372735, status=TreeStatus.DONE),
        Tree(id=2, xpos=48.207107, ypos=16.374865, status=TreeStatus.IN_PLANNING),
        Tree(id=3, xpos=48.208426, ypos=16.374076, status=TreeStatus.LOW_POTENTIAL),
        Tree(id=4, xpos=48.208951, ypos=16.372139, status=TreeStatus.MEDIUM_POTENTIAL),
        Tree(id=5, xpos=48.20819, ypos=16.370916, status=TreeStatus.HIGH_POTENTIAL),
        Tree(id=6, xpos=48.20755, ypos=16.373041, status=TreeStatus.HIGH_POTENTIAL),
        Tree(
            id=7,
            xpos=48.209399,
            ypos=16.373164,
            status=TreeStatus.HIGH_POTENTIAL,
            sponsor="Autofahrer",
        ),
    ]

    donations = [
        Donation(
            amount=random.randint(10, 50) + random.randint(0, 100) / 10,
            tree_id=sample(trees, 1)[0].id,
            user_username=sample(users, 1)[0].username,
        ),
        Donation(
            amount=random.randint(10, 50) + random.randint(0, 100) / 10,
            tree_id=sample(trees, 1)[0].id,
            user_username=sample(users, 1)[0].username,
        ),
        Donation(
            amount=random.randint(10, 50) + random.randint(0, 100) / 10,
            tree_id=sample(trees, 1)[0].id,
            user_username=sample(users, 1)[0].username,
        ),
        Donation(
            amount=random.randint(10, 50) + random.randint(0, 100) / 10,
            tree_id=sample(trees, 1)[0].id,
            user_username=sample(users, 1)[0].username,
        ),
    ]

    votes = [
        Vote(user_username=user.username, tree_id=tree.id)
        for user, tree in sample(list(zip(users, trees)), 5)
    ]

    with Session(engine) as session:
        for user in users:
            print(f"Adding user {user} to db.")
            session.add(user)

        for tree in trees:
            print(f"Adding tree {tree} to db.")
            session.add(tree)

        for donation in donations:
            print(f"Adding donation {donation} to db.")
            session.add(donation)

        for vote in votes:
            print(f"Adding vote {vote} to db.")
            session.add(vote)

        session.commit()

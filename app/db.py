import enum
import functools
from typing import List, Optional

from sqlalchemy import ForeignKey, Integer, LargeBinary, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

__engine = None


@functools.wraps(create_engine)
def get_engine(**kwargs):
    global __engine

    if __engine is None:
        __engine = create_engine("sqlite:///test.db", **kwargs)

    return __engine


class Role(enum.Enum):
    NORMAL_USER = 0
    ADMIN = 1


class TreeStatus(enum.Enum):
    DONE = 0
    IN_PLANNING = 1
    POTENTIAL = 2


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(30), primary_key=True)

    password_hash: Mapped[bytes] = mapped_column(LargeBinary(60))
    password_salt: Mapped[bytes] = mapped_column(LargeBinary(29))

    role: Mapped[Role] = mapped_column()

    donations: Mapped[List["Donation"]] = relationship(back_populates="user")

    votes: Mapped[List["Vote"]] = relationship(back_populates="user")


class Tree(Base):
    __tablename__ = "tree"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    xpos: Mapped[float]
    ypos: Mapped[float]
    status: Mapped[TreeStatus]

    donations: Mapped[List["Donation"]] = relationship(back_populates="tree")
    sponsor: Mapped[Optional[str]] = mapped_column(default=None)

    votes: Mapped[List["Vote"]] = relationship(back_populates="tree")


class Donation(Base):
    __tablename__ = "donation"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[int]

    tree_id: Mapped[int] = mapped_column(ForeignKey("tree.id"))
    tree: Mapped[Tree] = relationship(back_populates="donations")

    user_username: Mapped[User] = mapped_column(ForeignKey("user.username"))
    user: Mapped[User] = relationship(back_populates="donations")


class Vote(Base):
    __tablename__ = "vote"

    user_username: Mapped[str] = mapped_column(
        ForeignKey("user.username"), primary_key=True
    )
    user: Mapped[User] = relationship(back_populates="votes")

    tree_id: Mapped[int] = mapped_column(ForeignKey("tree.id"), primary_key=True)
    tree: Mapped[Tree] = relationship(back_populates="votes")


def fetch_user_from_db(username: str) -> User | None:
    statement = select(User).where(User.username.is_(username))

    with Session(get_engine()) as session:
        return session.scalar(statement)


def fetch_all_trees_from_db() -> dict:
    with Session(get_engine()) as session:
        # forgive me
        stm_all_trees = select(Tree)
        stm_all_votes = select(Vote)
        stm_crowdfund_money = select(Donation)

        trees = session.scalars(stm_all_trees).fetchall()
        votes = session.scalars(stm_all_votes).fetchall()
        donations = session.scalars(stm_crowdfund_money).fetchall()

        tree_votes = {
            tree.id: len(list(filter(lambda v: v.tree_id == tree.id, votes)))
            for tree in trees
        }

        tree_donations = {
            tree.id: sum(
                map(
                    lambda d: d.amount,
                    (filter(lambda v: v.tree_id == tree.id, donations)),
                )
            )
            for tree in trees
        }

        return {
            "trees": [
                {
                    "id": tree.id,
                    "xpos": tree.xpos,
                    "ypos": tree.ypos,
                    "sponsor": tree.sponsor,
                    "votes": tree_votes.get(tree.id),
                    "donations": tree_donations.get(tree.id),
                }
                for tree in trees
            ]
        }


def fetch_all_votes_for_user(username: str):
    with Session(get_engine()) as session:
        stm_users_votes = select(Vote).where(Vote.user_username.is_(username))

        votes = session.scalars(stm_users_votes).fetchall()

        return {"votes": [vote.tree_id for vote in votes], "username": username}


def add_vote_for_user(username: str, tree_id: int):
    with Session(get_engine()) as session:
        stm_users_votes = select(Vote).where(
            Vote.user_username.is_(username) and Vote.tree_id.is_(tree_id)
        )

        # we have it already
        if session.scalar(stm_users_votes):
            return

        vote = Vote(
            user_username=username,
            tree_id=tree_id,
        )

        session.add(vote)

        session.commit()


def add_user_donation(username: str, tree_id: int, amount: float):
    with Session(get_engine()) as session:
        donation = Donation(user_username=username, amount=amount, tree_id=tree_id)
        session.add(donation)
        session.commit()

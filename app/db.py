import enum
import functools
from typing import List

from sqlalchemy import ForeignKey, LargeBinary, String, create_engine, select
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


class Tree(Base):
    __tablename__ = "tree"

    id: Mapped[int] = mapped_column(primary_key=True)

    xpos: Mapped[float]
    ypos: Mapped[float]

    donations: Mapped[List["Donation"]] = relationship(back_populates="tree")


class Donation(Base):
    __tablename__ = "donation"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[int]

    tree_id: Mapped[int] = mapped_column(ForeignKey("tree.id"))
    tree: Mapped[Tree] = relationship(back_populates="donations")

    user_username: Mapped[User] = mapped_column(ForeignKey("user.username"))
    user: Mapped[User] = relationship(back_populates="donations")


def fetch_user_from_db(username: str) -> User | None:
    statement = select(User).where(User.username.is_(username))

    with Session(get_engine()) as session:
        return session.scalar(statement)

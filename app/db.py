import enum
import functools

from sqlalchemy import LargeBinary, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

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


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(30), primary_key=True)

    password_hash: Mapped[bytes] = mapped_column(LargeBinary(60))
    password_salt: Mapped[bytes] = mapped_column(LargeBinary(29))

    role: Mapped[Role] = mapped_column()


def fetch_user_from_db(username: str) -> User | None:
    statement = select(User).where(User.username.is_(username))

    with Session(get_engine()) as session:
        return session.scalar(statement)

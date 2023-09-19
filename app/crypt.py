import bcrypt


def generate_salt():
    return bcrypt.gensalt()


def hash_password(password: str, salt: bytes):
    return bcrypt.hashpw(password.encode(), salt)


def password_matches(password: str, salt: bytes, stored_hash: bytes):
    hashh = hash_password(password, salt)

    return hashh == stored_hash

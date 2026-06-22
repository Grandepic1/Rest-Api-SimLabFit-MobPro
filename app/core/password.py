from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError


password_hasher = PasswordHasher()


def is_password_hash(value: str) -> bool:
    return value.startswith("$argon2")


def hash_password(password: str) -> str:
    if is_password_hash(password):
        return password

    return password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return password_hasher.verify(password_hash, password)
    except (InvalidHashError, VerificationError, VerifyMismatchError):
        return False

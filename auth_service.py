from datetime import datetime, timedelta, timezone

from jose import jwt

from config import ACCESS_TOKEN_MINUTES, ALGORITHM, SECRET_KEY
from models.data import users


def authenticate(username: str, password: str):
    user = users.get(username)

    if user is None:
        return None

    if user["password"] != password:
        return None

    return user


def create_access_token(user: dict):
    expires = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_MINUTES
    )
    payload = {
        "sub": user["username"],
        "role": user["role"],
        "exp": expires,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

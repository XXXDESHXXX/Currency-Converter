from database import cur, conn
from services.io import AbstractAuthIO
from services.selectors.user import get_user


def create_user(username: str, password: str) -> None:
    cur.execute(
        f"""
        INSERT INTO auth_user (username, password) 
        VALUES ('{username}', '{password}');
        """
    )
    conn.commit()


def authenticate(username: str, password: str) -> tuple[int, str, str] | None:
    user = get_user(username)
    if user is None or user[2] != password:
        return None
    return user


def log_in(auth_io: AbstractAuthIO) -> tuple[int, str, str]:
    user = authenticate(auth_io.get_username(), auth_io.get_password())
    if user is None:
        print("The user with the provided credentials was not found.")
        return log_in(auth_io)
    return user

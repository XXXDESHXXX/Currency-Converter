from database import cur, conn
from selectors import get_user


def create_user(username: str, password: str) -> None:
    cur.execute(
        f"""
        INSERT INTO auth_user (username, password) 
        VALUES ('{username}', '{password}');
        """
    )
    conn.commit()


def log_in(username: str, password: str) -> tuple[int, str, str] | None:
    user = get_user(username)
    if user is None or user[2] != password:
        return None
    return user

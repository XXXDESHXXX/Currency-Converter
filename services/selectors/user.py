from database import cur


def get_user(username: str) -> tuple[int, str, str] | None:
    cur.execute(
        f"""
        SELECT * FROM auth_user 
        WHERE username = '{username}'
        """
    )
    return cur.fetchone()

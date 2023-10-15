from database import cur


def get_user(username: str) -> tuple[int, str, str]:
    cur.execute(
        f"""
        SELECT * FROM auth_user 
        WHERE username = '{username}'
        """
    )
    user = cur.fetchone()
    return user

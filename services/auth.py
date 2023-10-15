import psycopg2
from database import cur, conn


def register(username, password):
    cur.execute(
        f"""
        INSERT INTO auth_user (username, password) 
        VALUES ('{username}', '{password}');
        """
    )
    conn.commit()


def log_in(username, password):
    query = cur.execute(
        f"""
        SELECT * FROM auth_user 
        WHERE username = '{username}'
        """
    )
    user = cur.fetchone()
    return user

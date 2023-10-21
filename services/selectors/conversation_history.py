from database import cur
from datetime import datetime


def get_conversation_history(user_id: int) -> list[tuple[int, str, str, float, datetime, int]]:
    cur.execute(
        f"""
        SELECT * FROM convertation_history 
        WHERE user_id = {user_id}
        ORDER BY created_at DESC
        """
    )
    return cur.fetchall()

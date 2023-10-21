from datetime import datetime

from database import cur, conn


def save_conversation(from_currency: str, to_currency: str, amount: float, created_at: datetime, user_id: int) -> None:
    cur.execute(
        f"""
        INSERT INTO convertation_history (from_currency, to_currency, amount, created_at, user_id) 
        VALUES ('{from_currency}', '{to_currency}', {amount}, '{created_at}', {user_id});
        """
    )
    conn.commit()

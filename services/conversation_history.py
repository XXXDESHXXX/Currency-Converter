from sqlalchemy import select
from models import ConversationHistory
from database import session_maker
from datetime import datetime


def save_conversation(from_currency: str, to_currency: str, amount: float, user_id: int) -> None:
    with session_maker() as session:
        conversation = ConversationHistory(
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount,
            user_id=user_id,
        )
        session.add(conversation)
        session.commit()
        session.refresh(conversation)

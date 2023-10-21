from sqlalchemy import select
from database import session_maker
from models import ConversationHistory


def get_conversation_history(user_id: int) -> list[ConversationHistory]:
    with session_maker() as session:
        query = (
            select(ConversationHistory)
            .where(ConversationHistory.user_id == user_id)
            .order_by(ConversationHistory.created_at.desc())
        )
        result = session.execute(query)
        return result.scalars().all()

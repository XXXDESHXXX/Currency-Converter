from datetime import datetime

from database import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "auth_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(48), unique=True)
    password: Mapped[str] = mapped_column(String(256))

    def __repr__(self):
        return (
            f"""
            User(
            {self.id=},
            {self.username=},
            {self.password=})
            """
        )


class ConversationHistory(Base):
    __tablename__ = "conversation_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    from_currency: Mapped[str] = mapped_column(String(16))
    to_currency: Mapped[str] = mapped_column(String(16))
    amount: Mapped[float]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    user_id: Mapped[int] = mapped_column(ForeignKey("auth_user.id"))

    def __repr__(self):
        return (
            f"""
            ConversationHistory(
            {self.id=},
            {self.from_currency=},
            {self.to_currency=},
            {self.amount=},
            {self.created_at=},
            {self.user_id=})
            """
        )

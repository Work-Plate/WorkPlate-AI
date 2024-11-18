from sqlalchemy import Column, Boolean, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class ChatbotMessage(Base):
    __tablename__ = "chatbot_message"

    id = Column(BigInteger, primary_key=True)
    is_bot = Column(Boolean, nullable=False)
    msg = Column(String(255), nullable=False)

    member_id = Column(BigInteger, ForeignKey("member.id"), unique=True)
    member = relationship("Member", back_populates="chatbot_messages")

    created_at = Column(String(255), nullable=False)
    modified_at = Column(String(255), nullable=False)

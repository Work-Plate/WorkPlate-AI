from sqlalchemy import Column, BigInteger, String, Enum
from sqlalchemy.orm import relationship

from config.database import Base
from model.enum.user_role import UserRole


class Member(Base):
    __tablename__ = "member"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255))
    password = Column(String(255))
    username = Column(String(255))
    user_role = Column(Enum(UserRole))

    details = relationship("MemberDetail", back_populates="member")
    works = relationship("WorkMember", back_populates="members")
    chatbot_messages = relationship("ChatbotMessage", back_populates="member")

    created_at = Column(String(255), nullable=False)
    modified_at = Column(String(255), nullable=False)

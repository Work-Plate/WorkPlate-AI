from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class WorkMember(Base):
    __tablename__ = "work_member"

    id = Column(BigInteger, primary_key=True)

    member_id = Column(BigInteger, ForeignKey("member.id"))
    members = relationship("Member", back_populates="works")
    work_id = Column(BigInteger, ForeignKey("work.id"), unique=True)
    work = relationship("Work", back_populates="members")

    created_at = Column(String(255), nullable=False)
    modified_at = Column(String(255), nullable=False)
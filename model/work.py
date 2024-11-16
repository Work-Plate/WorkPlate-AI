from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship

from config.database import Base

class Work(Base):
    __tablename__ = "work"

    id = Column(BigInteger, primary_key=True)
    work_name = Column(String(255))
    work_detail = Column(String(255))
    work_credit = Column(BigInteger)

    members = relationship("WorkMember", back_populates="work")

    created_at = Column(String(255), nullable=False)
    modified_at = Column(String(255), nullable=False)
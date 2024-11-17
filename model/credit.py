from sqlalchemy import Column, BigInteger, String, ForeignKey

from config.database import Base


class Credit(Base):
    __tablename__ = "credit"

    id = Column(BigInteger, primary_key=True)
    balance = Column(BigInteger, default=0, nullable=False)

    member_id = Column(BigInteger, ForeignKey("member.id"), unique=True)

    created_at = Column(String(255), nullable=False)
    modified_at = Column(String(255), nullable=False)

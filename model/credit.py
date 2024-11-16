from sqlalchemy import Column, BigInteger, String

from config.database import Base


class Credit(Base):
    id = Column(BigInteger, primary_key=True)
    balance = Column(BigInteger, default=0, nullable=False)

    created_at = Column(String(255), nullable=False)
    modified_at = Column(String(255), nullable=False)

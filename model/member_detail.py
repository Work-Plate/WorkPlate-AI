from sqlalchemy import Column, BigInteger, ForeignKey, String, Enum
from sqlalchemy.orm import relationship

from config.database import Base
from model.enum.physical_status import PhysicalStatus
from model.enum.work_main_category import WorkMainCategory
from model.enum.work_sub_category import WorkSubCategory


class MemberDetail(Base):
    __tablename__ = "member_detail"

    id = Column(BigInteger, primary_key=True)
    age = Column(BigInteger, nullable=False)
    location = Column(String, nullable=False)
    main_experience = Column(Enum(WorkMainCategory))
    main_preference = Column(Enum(WorkMainCategory))
    physical_status = Column(Enum(PhysicalStatus))
    sub_experience = Column(Enum(WorkSubCategory))
    sub_preference = Column(Enum(WorkSubCategory))

    member_id = Column(BigInteger, ForeignKey("member.id"), unique=True)
    member = relationship("Member", back_populates="details", uselist=False)

    created_at = Column(String(255), nullable=False)
    modified_at = Column(String(255), nullable=False)

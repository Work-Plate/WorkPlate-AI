from sqlalchemy import Column, BigInteger, String, Enum, Integer
from sqlalchemy.orm import relationship

from config.database import Base
from model.enum.physical_status import PhysicalStatus
from model.enum.salary_type import SalaryType
from model.enum.work_main_category import WorkMainCategory
from model.enum.work_sub_category import WorkSubCategory


class Work(Base):
    __tablename__ = "work"

    id = Column(BigInteger, primary_key=True)
    location = Column(String(255), nullable=False)
    main_category = Column(Enum(WorkMainCategory), nullable=False)
    sub_category = Column(Enum(WorkSubCategory), nullable=False)
    physical_status = Column(Enum(PhysicalStatus), nullable=False)
    work_name = Column(String(255))
    work_detail = Column(String(255))
    work_credit = Column(BigInteger)

    members = relationship("WorkMember", back_populates="work")

    created_at = Column(String(255), nullable=False)
    modified_at = Column(String(255), nullable=False)

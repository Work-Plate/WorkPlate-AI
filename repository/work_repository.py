from sqlalchemy.orm import Session

from model.enum.physical_status import PhysicalStatus
from model.work import Work


class WorkRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_physical_status_and_location(self, physical_status: PhysicalStatus, location: str):
        return (
            self.session.query(Work)
            .filter(Work.physical_status == physical_status,
                    Work.location.like(f"{location}%")
            )
            .all()
        )

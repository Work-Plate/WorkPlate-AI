from sqlalchemy.orm import Session

from model.credit import Credit


class CreditRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_member_id(self, member_id: int) -> Credit:
        return self.session.query(Credit).filter(Credit.member_id == member_id).first()

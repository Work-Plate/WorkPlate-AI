from sqlalchemy.orm import Session

from model.credit import Credit
from model.member import Member


class CreditRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_username(self, username: str):
        return (
            self.session.query(Credit).join(Member)
            .filter(Member.username == username)
            .first()
        )

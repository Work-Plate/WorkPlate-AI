from sqlalchemy.orm import Session

from model.member import Member
from model.member_detail import MemberDetail


class MemberDetailRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_username(self, username: str):
        return (
            self.session.query(MemberDetail).join(Member)
            .filter(Member.username == username)
            .first()
        )

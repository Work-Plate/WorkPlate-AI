from sqlalchemy.orm import Session

from model.member_detail import MemberDetail


class MemberDetailRepository:
    def __init__(self, session: Session):
        self.session = session

    def find_by_member_id(self, member_id: int):
        return (
            self.session.query(MemberDetail)
            .filter(MemberDetail.member_id == member_id)
            .first()
        )
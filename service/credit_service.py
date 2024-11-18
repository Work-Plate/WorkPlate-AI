from repository.credit_repository import CreditRepository


class CreditService:
    def __init__(self, credit_repository: CreditRepository):
        self.credit_repository = credit_repository

    def get_credit_balance(self, member_id: int) -> int:
        """
        사용자 ID(member_id)를 입력받아, 엽전 정보 조회하는 서비스
        :param member_id: 사용자의 id
        :return: 사용자의 엽전 정보
        """
        return self.credit_repository.find_by_member_id(member_id).balance

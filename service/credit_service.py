from repository.credit_repository import CreditRepository


class CreditService:
    def __init__(self, credit_repository: CreditRepository):
        self.credit_repository = credit_repository

    def get_credit_balance(self, username: str) -> int:
        """
        사용자 ID(member_id)를 입력받아, 엽전 정보 조회하는 서비스
        :param username: 사용자의 이름
        :return: 사용자의 엽전 정보
        """
        return self.credit_repository.find_by_username(username).balance

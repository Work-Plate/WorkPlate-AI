from repository.credit_repository import CreditRepository

## 사용자 ID(member_id)를 입력받아, 엽전 정보 조회하는 서비스

class CreditService:
    def __init__(self, member_id:int):
        self.member_id = member_id

    def get_credit_balance(self): #  엽전 크레딧 잔액을 조회하는 서비스
        credit = CreditRepository()
        return credit.find_by_member_id(self.member_id).balance

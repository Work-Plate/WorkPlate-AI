from ai_model.gpt_model import GPTModel
from repository.work_repository import WorkRepository
# 사용

class WorkService:
    # WorkRepository의 find_by_physical_status_and_location-> 5개, 10개
    def __init__(self, gpt_model: GPTModel, member_id: int):
        self.gpt_model = gpt_model
        self.member_id = member_id
    def recommend(self):
        work_id_list = []
        # WorkRepository 기준으로 손봐야 함.
        work_repo = WorkRepository()
        work_lst = work_repo.find_by_physical_status_and_location(self.member_id)
        # 필터링하기
        # 선호 직종 -> 소분류 일치
        ## 기존 경험 -> 소분류 일치
        ### N개가 없으면 대분류 일치"""

        return work_id_list
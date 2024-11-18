from entity.work import WorkIdList
from model.member_detail import MemberDetail
from repository.member_detail_repository import MemberDetailRepository
from repository.work_repository import WorkRepository


class WorkService:
    def __init__(self, member_detail_repository: MemberDetailRepository, work_repository: WorkRepository):
        self.member_detail_repository = member_detail_repository
        self.work_repository = work_repository

    def recommend(self, username: str) -> WorkIdList:
        member_detail: MemberDetail = self.member_detail_repository.find_by_username(username)
        candidate_work_list = self.work_repository.find_by_physical_status_and_location(member_detail.physical_status, member_detail.location)

        work_list = []
        for work in candidate_work_list:
            if work.sub_category == member_detail.sub_preference:
                work_list.append(work.id)

        if len(work_list) <= 10:
            for work in candidate_work_list:
                if work.sub_category == member_detail.sub_experience:
                    work_list.append(work.id)

        if len(work_list) <= 10:
            for work in candidate_work_list:
                if work.id not in work_list and work.main_category == member_detail.main_preference:
                    work_list.append(work.id)

        if len(work_list) <= 10:
            for work in candidate_work_list:
                if work.id not in work_list and work.main_category == member_detail.main_experience:
                    work_list.append(work.id)

        return WorkIdList(job_id_list=work_list)

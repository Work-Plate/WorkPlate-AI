from entity.work import WorkIdList
from model.enum.physical_status import PhysicalStatus
from model.enum.work_sub_category import WorkSubCategory
from model.member_detail import MemberDetail
from repository.member_detail_repository import MemberDetailRepository
from repository.work_repository import WorkRepository


class WorkService:
    def __init__(self, member_detail_repository: MemberDetailRepository, work_repository: WorkRepository):
        self.member_detail_repository = member_detail_repository
        self.work_repository = work_repository

    def recommend(
            self,
            username: str,
            physical_status: PhysicalStatus | None,
            location: str | None,
            preference: WorkSubCategory | None,
            experience: WorkSubCategory | None
    ) -> WorkIdList:

        member_detail: MemberDetail = self.member_detail_repository.find_by_username(username)

        query_physical_status = physical_status if physical_status is not None else member_detail.physical_status
        query_location = location if location else member_detail.location
        query_sub_preference = preference if preference else member_detail.sub_preference
        query_sub_experience = experience if experience else member_detail.sub_experience

        candidate_work_list = (
            self.work_repository
            .find_by_physical_status_and_location(
                query_physical_status,
                query_location
            )
        )

        work_list = []
        for work in candidate_work_list:
            if work.sub_category == query_sub_preference:
                work_list.append(work.id)

        if len(work_list) <= 10:
            for work in candidate_work_list:
                if work.sub_category == query_sub_experience:
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

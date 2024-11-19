from enum import member

from dns.e164 import query

from entity.work import WorkIdList
from model.enum.physical_status import PhysicalStatus
from model.enum.work_main_category import WorkMainCategory
from model.enum.work_sub_category import WorkSubCategory
from model.member_detail import MemberDetail
from repository.member_detail_repository import MemberDetailRepository
from repository.work_repository import WorkRepository


class WorkService:
    def __init__(self, member_detail_repository: MemberDetailRepository, work_repository: WorkRepository):
        self.member_detail_repository = member_detail_repository
        self.work_repository = work_repository

    @staticmethod
    def _collect_recommendations(
            candidate_work_list: list,
            sub_preference: WorkSubCategory,
            sub_experience: WorkSubCategory,
            main_preference: WorkMainCategory,
            main_experience: WorkMainCategory
    ) -> list[int]:

        work_list = []
        criteria = [
            (lambda w: w.sub_category == sub_preference),
            (lambda w: w.sub_category == sub_experience),
            (lambda w: w.main_category == main_preference),
            (lambda w: w.main_category == main_experience),
        ]

        for condition in criteria:
            if len(work_list) >= 10:
                break

            for work in candidate_work_list:
                if work.id not in work_list and condition(work):
                    work_list.append(work.id)

                    if len(work_list) >= 10:
                        break

        return work_list

    def recommend(
            self,
            username: str,
            physical_status: PhysicalStatus | None,
            location: str | None,
            preference: WorkSubCategory | None,
            experience: WorkSubCategory | None
    ) -> WorkIdList:

        member_detail: MemberDetail = self.member_detail_repository.find_by_username(username)
        if not member_detail:
            raise ValueError(f"주어진 {username}으로 유저 상세 정보를 찾을 수 없습니다.")

        query_physical_status = physical_status if physical_status is not None else member_detail.physical_status
        query_location = location if location else member_detail.location
        if len(query_location.split()) >= 2:
            query_location = " ".join(query_location.split()[:2])
        query_sub_preference = preference if preference else member_detail.sub_preference
        query_sub_experience = experience if experience else member_detail.sub_experience

        candidate_work_list = (
            self.work_repository
            .find_by_physical_status_and_location(
                query_physical_status,
                query_location
            )
        )

        work_list = self._collect_recommendations(
            candidate_work_list,
            query_sub_preference,
            query_sub_experience,
            member_detail.main_preference,
            member_detail.main_experience
        )

        return WorkIdList(job_id_list=work_list)

from ai_model.gpt_model import GPTModel
from model.enum.physical_status import PhysicalStatus
from model.enum.work_sub_category import WorkSubCategory
from service.credit_service import CreditService
from entity.response_dto import ChatResponse
from prompt.chat_prompts import CHAT_WITH_BOT_TEMPLATE, USER_INTENTION_CLASSIFY_TEMPLATE, ENTITY_EXTRACTION_PROMPT
from service.work_service import WorkService


class ChatService:
    def __init__(self, gpt_model: GPTModel, work_service: WorkService, credit_service: CreditService):
        self.gpt_model = gpt_model
        self.work_service = work_service
        self.credit_service = credit_service

    def send_message(self, message: str):
        """
        사용자 message에 대한 텍스트 기반 응답을 생성합니다.
        :param message: 사용자의 메시지
        :return: 챗봇의 응답
        """
        try:
            prompt = CHAT_WITH_BOT_TEMPLATE
            response_text = self.gpt_model.generate_response(prompt, message)
            return response_text
        except Exception as e:
            raise Exception(f"OpenAI API -> 텍스트 응답 생성 중 오류 발생: {str(e)}")

    @staticmethod
    def create_profile(location: str, physical_status: str | None, experience: str | None,
                       preference: str | None) -> dict:
        return {
            "location": location,
            "physical_status": PhysicalStatus(physical_status) if physical_status is not None else None,
            "experience": WorkSubCategory(experience) if experience is not None else None,
            "preference": WorkSubCategory(preference) if preference is not None else None
        }

    def extract_entities(self, user_message: str):
        """
        user_message를 기반으로 노쇠 정도, 기존 경험, 선호 직종을 추출합니다.
        :param user_message: 사용자 메시지
        :return: location, physical_status, experience, preference 를 포함한 딕셔너리
        """
        try:
            prompt = ENTITY_EXTRACTION_PROMPT
            entity_str = self.gpt_model.generate_response(prompt, user_message)  # "<Location> <신체상태> <기존경험> <선호경험>"
            response = entity_str.replace('"', '').replace("\"", "")  # '이나 " 제거
            location, physical_status, experience, preference = [
                None if x == "UNKNOWN" else x
                for x in response.split(', ')
            ]
            return self.create_profile(location=location,
                                       physical_status=physical_status,
                                       experience=experience,
                                       preference=preference)
        except Exception as e:
            raise Exception(f"OpenAI API -> 유저 엔티티 추출 중 오류 발생: {str(e)}")

    def inference_user_intention(self, username: str, user_message: str) -> ChatResponse:
        """
        3가지 타입으로 사용자 의도 분류(엽전 조회, 일거리 추천, 일반 대화)
        :param username: 사용자의 이름
        :param user_message: 사용자의 메시지
        :return: 챗봇의 응답
        """
        user_intention = self.gpt_model.generate_response(USER_INTENTION_CLASSIFY_TEMPLATE,
                                                          user_message)  # 사용자 대화 의도
        # user_intention 별 대화 실행(Work_Recommendation, Credit_Inquiry, General_Conversation)
        if user_intention == "Work_Recommendation":
            # 유저 응답에서 엔티티 추출
            entities = self.extract_entities(user_message)
            physical_status, location, preference, experience = entities['physical_status'], entities['location'], entities['preference'], entities['experience']
            work_list = self.work_service.recommend(username, physical_status, location, preference, experience)
            return ChatResponse(**{
                "task_type": "job_recommend",
                "text": "일자리를 추천해드릴게요.",
                "additional_data": work_list
            })
        elif user_intention == "Credit_Inquiry":
            balance = self.credit_service.get_credit_balance(username)
            response_text = f"잔여 엽전을 조회해드릴게요.\n 잔여 엽전 크레딧은 {balance}입니다. "
        else:
            response_text = self.send_message(user_message)

        return ChatResponse(**{
            "task_type": "conversation",
            "text": response_text,
            "additional_data": None
        })



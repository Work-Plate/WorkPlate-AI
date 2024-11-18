from ai_model.gpt_model import GPTModel
from prompt.chat_prompts import CHAT_WITH_BOT_TEMPLATE, USER_INTENTION_CLASSIFY_TEMPLATE
from credit_service import CreditService
from work_service import WorkService


class ChatService:
    def __init__(self, gpt_model: GPTModel):
        self.gpt_model = gpt_model

    def send_message(self, message: str):
        """
        사용자 메시지와 이전 대화 내용이 주어지면 챗봇의 응답을 생성합니다.
        :param message: 이번에 보낼 사용자의 메시지
        :return: 챗봇의 응답
        """
        # 사용자 message에 대한 텍스트 기반 응답 생성
        try:
            prompt = CHAT_WITH_BOT_TEMPLATE
            response_text = self.gpt_model.generate_response(prompt, message)
            return response_text
        except Exception as e:
            raise Exception(f"OpenAI API -> 텍스트 응답 생성 중 오류 발생: {str(e)}")

    def inference_user_intention(self, user_message: str):  # 3가지 타입으로 사용자 의도 분류(엽전 조회, 일거리 추천, 일반 대화)
        response_text = ''
        user_intention = self.gpt_model.generate_response(USER_INTENTION_CLASSIFY_TEMPLATE,
                                                          user_message)  # 사용자 대화 의도
        # user_intention: Work_Recommendation, Credit_Inquiry, General_Conversation
        if user_intention == "Work_Recommendation":
            # 반환 받는 코드 작성 해야함
            return
        elif user_intention == "Credit_Inquiry":
            credit_service = CreditService(self.member_id)
            balance = credit_service.get_credit_balance()
            response_text = f"잔여 엽전을 조회해드릴게요.\n 잔여 엽전 크레딧은 {balance}입니다. "
        else:
            response_text = self.send_message(user_message)

        return response_text

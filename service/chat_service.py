from ai_model.gpt_model import GPTModel
from entity.chatbot_message import Message
from prompt.chat_prompts import CHAT_WITH_BOT_TEMPLATE


class ChatService:
    def __init__(self, gpt_model: GPTModel):
        self.gpt_model = gpt_model

    def send_message(self, message: str, prev_messages: list[Message]):
        """
        사용자 메시지와 이전 대화 내용이 주어지면 챗봇의 응답을 생성합니다.
        :param message: 이번에 보낼 사용자의 메시지
        :param prev_messages: 이전에 챗봇과 했던 대화내용
        :return: 챗봇의 응답
        """
        prev_messages.sort(key=lambda x: x.createdAt)
        prev_message = '\n'.join([msg.msg for msg in prev_messages])

        prompt = CHAT_WITH_BOT_TEMPLATE.format(previous_messages=prev_message)
        response = self.gpt_model.generate_response(prompt, message)

        return response
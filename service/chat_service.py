from entity.chatbot_message import Message
from model.gpt_model import GPTModel


class ChatService:
    def __init__(self, gpt_model: GPTModel):
        self.gpt_model = gpt_model
        with open("prompt/chat_with_bot", "rt") as f:
            self.chat_with_bot_template = f.read()

    def send_message(self, message: str, prev_messages: list[Message]):
        prev_messages.sort(key=lambda x: x.createdAt)
        prev_message = '\n'.join([msg.msg for msg in prev_messages])

        prompt = self.chat_with_bot_template.format(previous_messages=prev_message)
        response = self.gpt_model.generate_response(prompt, message)

        return response
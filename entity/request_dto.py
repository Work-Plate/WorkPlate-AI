from pydantic import BaseModel

from entity.chatbot_message import Message


class ChatRequest(BaseModel):
    username: str
    msg: str
    prevMsg: list[Message]

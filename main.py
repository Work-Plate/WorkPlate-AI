from datetime import datetime

from fastapi import FastAPI

from entity.request_dto import ChatRequest
from entity.response_dto import ChatResponse
from model.gpt_model import GPTModel
from service.chat_service import ChatService

gpt_model = GPTModel()
chat_service = ChatService(gpt_model)

app = FastAPI()

@app.post("/ai/chatbot")
async def chat(request: ChatRequest):
    """
    사용자 메시지와 이전 대화 내용이 주어지면 챗봇의 응답을 반환합니다.
    :param request: 사용자 정보, 이전 대화 내용, 메시지
    :return: 챗봇 응답
    """
    response = {
        "success": True,
        "message": "챗봇 응답 결과",
        "data": chat_service.send_message(request.msg, request.prevMsg)
    }

    return ChatResponse(**response)

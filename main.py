from fastapi import FastAPI

from ai_model.gpt_model import GPTModel
from config.database import Session
from entity.request_dto import ChatRequest
from repository.credit_repository import CreditRepository
from repository.member_detail_repository import MemberDetailRepository
from repository.work_repository import WorkRepository
from service.chat_service import ChatService
from service.credit_service import CreditService
from service.work_service import WorkService

session = Session()

gpt_model = GPTModel()

credit_repository = CreditRepository(session)
member_detail_repository = MemberDetailRepository(session)
work_repository = WorkRepository(session)

credit_sevice = CreditService(credit_repository)
work_service = WorkService(member_detail_repository, work_repository)

chat_service = ChatService(gpt_model, work_service, credit_sevice)

app = FastAPI()

@app.post("/ai/chatbot")
async def chat(request: ChatRequest):
    """
    사용자 메시지가 주어지면 의도를 파악하여 적절한 답을 내놓습니다.
    :param request: 사용자 ID, 메시지
    :return: 챗봇 응답
    """
    response = chat_service.inference_user_intention(request.member_id, request.user_message)

    return response

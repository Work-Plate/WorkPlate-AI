import traceback

from fastapi import FastAPI
from openai import OpenAIError
from starlette.responses import JSONResponse

from ai_model.gpt_model import GPTModel
from config.database import Session
from config.log import get_logger
from entity.request_dto import ChatRequest
from repository.credit_repository import CreditRepository
from repository.member_detail_repository import MemberDetailRepository
from repository.work_repository import WorkRepository
from service.chat_service import ChatService
from service.credit_service import CreditService
from service.work_service import WorkService
from utils.init_db import create_tables

session = Session()
create_tables()

gpt_model = GPTModel()

credit_repository = CreditRepository(session)
member_detail_repository = MemberDetailRepository(session)
work_repository = WorkRepository(session)

credit_sevice = CreditService(credit_repository)
work_service = WorkService(member_detail_repository, work_repository)

chat_service = ChatService(gpt_model, work_service, credit_sevice)

logger = get_logger()

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_handler(request, exc: ValueError):
    error_details = traceback.format_exc()
    logger.error(f"Stack Trace:\n{error_details}")
    logger.error(f"An error occerred: {str(exc)}")

    return JSONResponse(
        status_code=400,
        content={"message": str(exc)}
    )

@app.exception_handler(OpenAIError)
async def openai_error_handler(request, exc: OpenAIError):
    error_details = traceback.format_exc()
    logger.error(f"Stack Trace:\n{error_details}")
    logger.error(f"An error occerred: {str(exc)}")

    return JSONResponse(
        status_code=400,
        content={"message": "OpenAI Error입니다. 관리자에게 문의하세요."}
    )

@app.exception_handler(Exception)
async def value_error_handler(request, exc: Exception):
    error_details = traceback.format_exc()
    logger.error(f"Stack Trace:\n{error_details}")
    logger.error(f"An error occerred: {str(exc)}")

    return JSONResponse(
        status_code=400,
        content={"message": "예상치 못한 Error입니다. 관리자에게 문의하세요"}
    )

@app.post("/ai/chatbot")
async def chat(request: ChatRequest):
    """
    사용자 메시지가 주어지면 의도를 파악하여 적절한 답을 내놓습니다.
    :param request: 사용자 ID, 메시지
    :return: 챗봇 응답
    """
    response = chat_service.inference_user_intention(request.username, request.user_message)

    return response

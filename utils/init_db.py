from config.database import engine
from model.chatbot_message import ChatbotMessage
from model.credit import Credit
from model.member import Member
from model.member_detail import MemberDetail
from model.work import Work


def create_tables():
    Member.metadata.create_all(bind=engine)
    MemberDetail.metadata.create_all(bind=engine)
    Work.metadata.create_all(bind=engine)
    ChatbotMessage.metadata.create_all(bind=engine)
    Credit.metadata.create_all(bind=engine)

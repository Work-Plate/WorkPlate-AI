from pydantic import BaseModel

from entity.work import WorkIdList


class ChatResponse(BaseModel):
    task_type: str
    text: str
    additional_data: WorkIdList | None

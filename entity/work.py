from pydantic import BaseModel

class WorkIdList(BaseModel):
    job_id_list: list[int]

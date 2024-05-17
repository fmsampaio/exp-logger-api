from datetime import datetime
from pydantic import BaseModel


class ProjectShow(BaseModel):
    id: int
    title: str
    description: str

    class Config():
        #orm_mode = True
        from_attributes=True

class ProjectCreate(BaseModel):
    title: str
    description: str

class LogEntryShow(BaseModel):
    experiment_name: str
    log_message: str
    log_details: str
    time_created: datetime
    project: ProjectShow
    
    class Config():
        #orm_mode = True
        from_attributes=True

class LogEntryCreate(BaseModel):
    experiment_name: str
    log_message: str
    log_details: str
    project_id: int
    
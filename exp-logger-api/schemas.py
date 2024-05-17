from datetime import datetime
from pydantic import BaseModel

class LogEntryShow(BaseModel):
    id: int
    experiment_name: str
    log_message: str
    log_details: str
    time_created: datetime

class LogEntryCreate(BaseModel):
    experiment_name: str
    log_message: str
    log_details: str
    
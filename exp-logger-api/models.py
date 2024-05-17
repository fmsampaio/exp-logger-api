from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

import datetime

from .database import Base

class LogEntry(Base):
    __tablename__ = 'log_entries_db'
    id = Column(Integer, primary_key = True, index = True)
    experiment_name = Column(String)
    log_message = Column(String)
    log_details = Column(String)
    time_created = Column(DateTime(timezone=True), default=func.now())

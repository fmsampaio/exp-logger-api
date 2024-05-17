from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

import datetime

from .database import Base

class LogEntry(Base):
    __tablename__ = 'db_log_entries'
    id = Column(Integer, primary_key = True, index = True)
    experiment_name = Column(String)
    log_message = Column(String)
    log_details = Column(String)
    time_created = Column(DateTime(timezone=True), default=func.now())

    project_id = Column(Integer, ForeignKey('db_projects.id'))
    project = relationship("Project")


class Project(Base):
    __tablename__ = 'db_projects'
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    description = Column(String)

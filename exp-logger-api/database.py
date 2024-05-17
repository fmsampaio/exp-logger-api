from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = 'sqlite:///./exp-logger.db'
DATABASE_URL = 'postgresql://ueo8uc57lmfe61:p4c1dc2568af90009881047aa3d794cc0aa36df7f51a8d8893ab2eac134cef980@ceqbglof0h8enj.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d95bp6njkiql5j'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
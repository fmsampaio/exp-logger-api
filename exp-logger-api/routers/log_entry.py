from fastapi import status, APIRouter, Depends

from ..database import SessionLocal, get_db
from .. import schemas, models

router = APIRouter(
    tags = ['Log Entries'],
    prefix= '/log_entries'
)

@router.get('/', response_model=list[schemas.LogEntryShow])
def list_all(db: SessionLocal = Depends(get_db)):
    log_entries = db.query(models.LogEntry).all()
    return log_entries

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.LogEntryCreate, db: SessionLocal = Depends(get_db)):
    newLogEntry = models.LogEntry(
        experiment_name = request.experiment_name,
        log_message = request.log_message,
        log_details = request.log_details,
        project_id = request.project_id
    )
    db.add(newLogEntry)
    db.commit()
    db.refresh(newLogEntry)

    return newLogEntry
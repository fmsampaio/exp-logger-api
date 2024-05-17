from fastapi import status, APIRouter, Depends

from ..database import SessionLocal, get_db
from .. import schemas, models

router = APIRouter(
    tags = ['Projects'],
    prefix= '/projects'
)

@router.get('/', response_model=list[schemas.ProjectShow])
def list_all(db: SessionLocal = Depends(get_db)):
    projects = db.query(models.Project).all()
    return projects

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.ProjectCreate, db: SessionLocal = Depends(get_db)):
    newProject = models.Project(
        title = request.title,
        description = request.description
    )
    
    db.add(newProject)
    db.commit()
    db.refresh(newProject)

    return newProject

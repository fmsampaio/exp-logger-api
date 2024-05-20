from .. import models
from fastapi import status, HTTPException

def checkProjectById(id, db):
    query = db.query(models.Project).filter(models.Project.id == id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Project with id equals to {id} was not found.')
    return query
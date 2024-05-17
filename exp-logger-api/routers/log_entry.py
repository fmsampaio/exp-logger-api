from fastapi import APIRouter

router = APIRouter(
    tags = ['Log Entries'],
    prefix= '/logs'
)

@router.get('/')
def list_all():
    return {
        'info' : 'List all log entries route is not implemented yet!'
    }
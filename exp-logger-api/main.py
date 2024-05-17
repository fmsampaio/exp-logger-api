from fastapi import FastAPI
from .database import Base, engine
from .routers import log_entry, project

from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(log_entry.router)
app.include_router(project.router)

@app.get('/')
def index():
    return {
        'info' : 'API for logging computational experiments status'
    }


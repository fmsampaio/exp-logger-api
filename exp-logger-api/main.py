from fastapi import FastAPI
from .database import Base, engine
from .routers import log_entry

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(log_entry.router)

@app.get('/')
def index():
    return {
        'info' : 'API for logging computational experiments status'
    }


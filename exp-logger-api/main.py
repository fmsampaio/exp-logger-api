from fastapi import FastAPI
from .database import Base, engine

app = FastAPI()

Base.metadata.create_all(engine)

@app.get('/')
def index():
    return {
        'info' : 'API for logging computational experiments status'
    }
import uvicorn
from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.tables import Base
from models.config_database import engine


# Create NoteRequest Base Model
class NoteRequest(BaseModel):
    note: str

# Create the database
Base.metadata.create_all(engine)


app = FastAPI()



@app.get("/")
async def root():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return {"message": f"Hello World, today is {d1}"}

if __name__ == "__main__":
    uvicorn.run("main:app")
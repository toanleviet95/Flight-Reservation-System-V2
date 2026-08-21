from fastapi import FastAPI
from sqlmodel import SQLModel
from app.api import users, flights
from app.core.config import engine
from app import models

app = FastAPI(title = "FastAPI: Flight Reservation System", description = "API for flight reservation system", version = "1.0.0")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(users.router)
app.include_router(flights.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Flight Reservation System"}
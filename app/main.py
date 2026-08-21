from fastapi import FastAPI
from sqlmodel import SQLModel

from app.api.v1.api import api_router
from app.core.logging import setup_logging
from app.db.session import engine
import app.db.base  # noqa: F401 — registers all table models on SQLModel.metadata

setup_logging()

app = FastAPI(
    title="FastAPI: Flight Reservation System",
    description="API for flight reservation system",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup() -> None:
    SQLModel.metadata.create_all(engine)


app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root() -> dict:
    return {"message": "Welcome to the Flight Reservation System"}

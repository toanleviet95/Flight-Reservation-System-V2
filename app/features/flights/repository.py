"""
FlightRepository — data-access layer for the Flight entity.
Wraps raw SQLModel queries so that router/service code stays clean.
"""

from sqlmodel import Session, select
from app.features.flights.models import Flight
from app.features.flights.schemas import FlightCreate, FlightUpdate


class FlightRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self, offset: int = 0, limit: int = 100) -> list[Flight]:
        return list(self.session.exec(select(Flight).offset(offset).limit(limit)).all())

    def get_by_id(self, flight_id: int) -> Flight | None:
        return self.session.get(Flight, flight_id)

    def create(self, data: FlightCreate) -> Flight:
        flight = Flight.model_validate(data)
        self.session.add(flight)
        self.session.commit()
        self.session.refresh(flight)
        return flight

    def update(self, flight: Flight, data: FlightUpdate) -> Flight:
        patch = data.model_dump(exclude_unset=True)
        for key, value in patch.items():
            setattr(flight, key, value)
        self.session.add(flight)
        self.session.commit()
        self.session.refresh(flight)
        return flight

    def delete(self, flight: Flight) -> None:
        self.session.delete(flight)
        self.session.commit()

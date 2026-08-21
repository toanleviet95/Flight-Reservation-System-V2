"""
FlightService — business-logic layer for flights.
Delegates persistence to FlightRepository.
"""

from fastapi import HTTPException, status
from sqlmodel import Session

from app.features.flights.repository import FlightRepository
from app.features.flights.schemas import FlightCreate, FlightRead, FlightUpdate
from app.features.flights.models import Flight


class FlightService:
    def __init__(self, session: Session) -> None:
        self.repo = FlightRepository(session)

    def list_flights(self, offset: int = 0, limit: int = 100) -> list[Flight]:
        return self.repo.get_all(offset=offset, limit=limit)

    def get_flight(self, flight_id: int) -> Flight:
        flight = self.repo.get_by_id(flight_id)
        if not flight:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Flight {flight_id} not found",
            )
        return flight

    def create_flight(self, data: FlightCreate) -> Flight:
        return self.repo.create(data)

    def update_flight(self, flight_id: int, data: FlightUpdate) -> Flight:
        flight = self.get_flight(flight_id)
        return self.repo.update(flight, data)

    def delete_flight(self, flight_id: int) -> None:
        flight = self.get_flight(flight_id)
        self.repo.delete(flight)

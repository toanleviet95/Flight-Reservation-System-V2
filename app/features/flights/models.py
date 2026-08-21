from typing import List, TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.features.bookings.models import Booking


class Flight(SQLModel, table=True):
    flight_id: int | None = Field(default=None, primary_key=True)
    flight_number: str | None = Field(default=None, max_length=255)
    airline_id: int | None = None
    departure_airport_id: int | None = None
    arrival_airport_id: int | None = None
    departure_time: str | None = None  # ISO 8601 string; use datetime after full setup
    arrival_time: str | None = None
    base_price: float | None = None
    aircraft_id: int | None = None
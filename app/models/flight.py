from typing import List
from datetime import datetime
from decimal import Decimal
from sqlmodel import SQLModel, Field, Relationship

class FlightBase(SQLModel):
    flight_number: str | None = Field(default=None, max_length=255)
    airline_id: int | None = None
    departure_airport_id: int | None = None
    arrival_airport_id: int | None = None
    departure_time: datetime | None = None
    arrival_time: datetime | None = None
    base_price: Decimal | None = Field(default=None, max_digits=10, decimal_places=0)
    aircraft_id: int | None = None

class Flight(FlightBase, table=True):
    flight_id: int | None = Field(default=None, primary_key=True)
    bookings: List["Booking"] = Relationship(back_populates="flight")

class FlightCreate(FlightBase):
    pass

class FlightRead(FlightBase):
    flight_id: int

class FlightUpdate(SQLModel):
    flight_number: str | None = None
    airline_id: int | None = None
    departure_airport_id: int | None = None
    arrival_airport_id: int | None = None
    departure_time: datetime | None = None
    arrival_time: datetime | None = None
    base_price: Decimal | None = None
    aircraft_id: int | None = None
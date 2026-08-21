from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List

from app.core.config import get_session
from app.models.flight import Flight, FlightCreate, FlightRead, FlightUpdate

router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)

@router.post("/", response_model=FlightRead, status_code=status.HTTP_201_CREATED)
def create_flight(*, session: Session = Depends(get_session), flight: FlightCreate):
    db_flight = Flight.model_validate(flight)
    session.add(db_flight)
    session.commit()
    session.refresh(db_flight)
    return db_flight

@router.get("/", response_model=List[FlightRead])
def read_flights(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    flights = session.exec(select(Flight).offset(offset).limit(limit)).all()
    return flights

@router.get("/{flight_id}", response_model=FlightRead)
def read_flight(*, session: Session = Depends(get_session), flight_id: int):
    flight = session.get(Flight, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.patch("/{flight_id}", response_model=FlightRead)
def update_flight(
    *,
    session: Session = Depends(get_session),
    flight_id: int,
    flight: FlightUpdate,
):
    db_flight = session.get(Flight, flight_id)
    if not db_flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    
    flight_data = flight.model_dump(exclude_unset=True)
    for key, value in flight_data.items():
        setattr(db_flight, key, value)
        
    session.add(db_flight)
    session.commit()
    session.refresh(db_flight)
    return db_flight

@router.delete("/{flight_id}")
def delete_flight(*, session: Session = Depends(get_session), flight_id: int):
    flight = session.get(Flight, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    
    session.delete(flight)
    session.commit()
    return {"ok": True}

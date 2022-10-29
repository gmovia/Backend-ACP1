from fastapi import APIRouter, Depends
from schemas.reservationSchema import ReservationSchema
from sqlalchemy.orm import Session
from controller import reservationController
from config.db import engine, get_db
from models import reservation

reservation.Base.metadata.create_all(bind=engine)

reservation = APIRouter()

@reservation.post('/reserve/', status_code=200)
def reserve(reservationSchema: ReservationSchema, db: Session = Depends(get_db)):
    return reservationController.reserve(reservationSchema, db)

@reservation.delete('/deleteReservation/', status_code=200)
def delete_reservation(email_user: str, reservation_id: int, db: Session = Depends(get_db)):
    return reservationController.delete(email_user, reservation_id, db)

@reservation.post('//')
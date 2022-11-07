from fastapi import APIRouter, Depends
from schemas.reservationSchema import *
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

@reservation.post('/fetchAllUserReservations/', status_code=200)
def fetch_all_user_reservation(email_user: str, db: Session = Depends(get_db)):
    return reservationController.fetch_by_user(email_user, db)

@reservation.post('/fetchReservationsFromOwner/')
def fetch_all_owner_reservation(email_user: str, db: Session = Depends(get_db)):
    return reservationController.fetch_all_owner_reservation(email_user, db)

@reservation.post('/getReservedDaysByDateRange/')
def get_reserved_days_by_date_range(query: ReservationSchema, db: Session = Depends(get_db)):
    return reservationController.fetch_reserved_days_by_date_range(query, db)
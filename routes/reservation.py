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

@reservation.post('/fetchAllReservationsFromProperty')
def fetch_all_reservations_from_property(property_id: int, db: Session = Depends(get_db)):
    return reservationController.fetch_all_reservations_from_property(property_id, db)

@reservation.post('/getReservedDaysByDateRange/', status_code=200)
def get_reserved_days_by_date_range(query: ReservationSchemaByDateRange, db: Session = Depends(get_db)):
    return reservationController.fetch_reserved_days_by_date_range(query, db)

@reservation.post('/reservationStatus/', status_code=200)
def get_reservation_status(publication_id: int, db: Session = Depends(get_db)):
    return reservationController.get_reservation_status(publication_id, db)
    

@reservation.post('/payReservation/', status_code=200)
def payReservation(reservation_id: int, db: Session = Depends(get_db)):
    return reservationController.payReservation(reservation_id, db)    

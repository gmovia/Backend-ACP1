from sqlalchemy.orm import Session
from schemas.reservationSchema import ReservationSchema
from models.reservation import Reservation
from datetime import datetime, timedelta

def create_reservation(user_id: int, price_per_day: int, reservationSchema: ReservationSchema, db: Session):
    db_reservation = Reservation(
                                    start_date=reservationSchema.start_date,
                                    end_date=reservationSchema.end_date,
                                    price=price_per_day*((reservationSchema.end_date-reservationSchema.start_date).days),
                                    publication_id=reservationSchema.publication_id,
                                    user_id=user_id
                                )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def is_the_property_reserved(publication_id: int, start_date: datetime, end_date: datetime, db: Session):
    days_list = [(start_date + timedelta(days=d)).strftime("%Y-%m-%d") for d in range((end_date - start_date).days + 1)] 
    for i in days_list:
        is_reserved = db.query(Reservation).filter(Reservation.publication_id == publication_id).filter(Reservation.start_date <= i).filter(i <= Reservation.end_date).first()
        if is_reserved is not None:
            return True
    return False
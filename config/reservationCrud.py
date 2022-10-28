from sqlalchemy.orm import Session
from schemas.reservationSchema import ReservationSchema
from models.reservation import Reservation
from datetime import datetime

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

def is_the_property_reserved(start_date: datetime, end_date: datetime, db: Session):
    #Implementar algoritmo que, dado un rango de fechas, diga si esta reservada la propiedad 
    return 0
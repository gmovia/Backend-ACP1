from sqlalchemy.orm import Session
from schemas.reservationSchema import ReservationSchema
from models.reservation import Reservation
from models.publication import Publication
from models.user import User
from models.propertie import Property
from datetime import datetime, timedelta

def get_reservation(reservation_id: int, db: Session):
    return db.query(Reservation).filter(Reservation.id == reservation_id).first()

def get_reservations_from_property(property_id: id, db: Session):
    return db.query(Reservation, User.email, User.name).join(Publication).filter(Publication.property_id == property_id).filter(Publication.id == Reservation.publication_id).filter(User.id == Reservation.user_id).all()

def get_reservations_by_user_id(user_id: int, db: Session):
    return db.query(Reservation).filter(Reservation.user_id == user_id).all()

def get_reservations_from_owner(user_id: int, db: Session):
    return db.query(Property, Publication, Reservation).filter(Reservation.publication_id == Publication.id).filter(Publication.property_id == Property.id).filter(Property.user_id == user_id).all()

def have_at_least_one_reservation(publication_id: int, db: Session):
    return db.query(Reservation).filter(Reservation.publication_id == publication_id).first()

def get_reserved_days_by_date_range(start_date: datetime, end_date: datetime, publication_id: int, db: Session):
    days_list = [(start_date + timedelta(days=d)).strftime("%Y-%m-%d") for d in range((end_date - start_date).days + 1)] 
    days_reserved = []
    for i in days_list:
        is_reserved = db.query(Reservation).filter(Reservation.publication_id == publication_id).filter(Reservation.start_date <= i).filter(i <= Reservation.end_date).first()
        if is_reserved is not None:
            days_reserved.append(i)
    return days_reserved

def create_reservation(user_id: int, price_per_day: int, reservationSchema: ReservationSchema, db: Session):
    db_reservation = Reservation(
                                    start_date=reservationSchema.start_date,
                                    end_date=reservationSchema.end_date,
                                    price=price_per_day*((reservationSchema.end_date-reservationSchema.start_date).days),
                                    publication_id=reservationSchema.publication_id,
                                    user_id=user_id,
                                    paid=False
                                )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def delete_reservation(db_reservation, db: Session):
    db.delete(db_reservation)
    db.commit()
    return db_reservation

def is_the_property_reserved(publication_id: int, start_date: datetime, end_date: datetime, db: Session):
    days_list = [(start_date + timedelta(days=d)).strftime("%Y-%m-%d") for d in range((end_date - start_date).days + 1)] 
    for i in days_list:
        is_reserved = db.query(Reservation).filter(Reservation.publication_id == publication_id).filter(Reservation.start_date <= i).filter(i <= Reservation.end_date).first()
        if is_reserved is not None:
            return True
    return False
    
def pay_reservation(reservation_id: int, db: Session):
    db_reservation = get_reservation(reservation_id, db)    
    db_reservation.paid = True
    db.add(db_reservation)
    db.commit()
    return db_reservation 

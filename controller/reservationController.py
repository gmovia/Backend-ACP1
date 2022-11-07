from fastapi import HTTPException
from config.userCrud import get_user
from config.publicationCrud import get_publication
from config.reservationCrud import *
from schemas.reservationSchema import *
from sqlalchemy.orm import Session

def reserve(reservationSchema: ReservationSchema, db: Session):
    db_user = get_user(db, reservationSchema.email_user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")
    
    db_publication = get_publication(db, reservationSchema.publication_id)
    
    if db_publication is None:
       raise HTTPException(status_code=400, detail="Permission denied.")

    if is_the_property_reserved(db_publication.id, reservationSchema.start_date, reservationSchema.end_date, db) is True:
        raise HTTPException(status_code=400, detail="The property is reserved.")

    return create_reservation(db_user.id, db_publication.price, reservationSchema, db)

def delete(email_user: str, reservation_id: int, db: Session):
    db_user = get_user(db, email_user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")

    db_reservation = get_reservation(reservation_id, db)

    if db_reservation is None or db_reservation.user_id != db_user.id:
        raise HTTPException(status_code=400, detail="Permission denied.")

    return delete_reservation(db_reservation, db)

def fetch_by_user(email_user, db: Session):
    db_user = get_user(db, email_user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")

    return get_reservations_by_user_id(db_user.id, db)

def fetch_reserved_days_by_date_range(query: ReservationSchema, db: Session):
    db_user = get_user(db, query.email_user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")

    db_publication = get_publication(db, query.publication_id)
    
    if db_publication is None:
       raise HTTPException(status_code=400, detail="Permission denied.")

    return get_reserved_days_by_date_range(query.start_date, query.end_date, query.publication_id, db)

def fetch_all_owner_reservation(email_user: str, db: Session):
    db_user = get_user(db, email_user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")
    
    return get_reservations_from_owner(db_user.id, db)
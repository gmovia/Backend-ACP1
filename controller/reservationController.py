from fastapi import HTTPException
from config.userCrud import get_user
from config.publicationCrud import get_publication
from config.reservationCrud import *
from schemas.reservationSchema import ReservationSchema
from sqlalchemy.orm import Session

def reserve(reservationSchema: ReservationSchema, db: Session):
    db_user = get_user(db, reservationSchema.email_user)

    if db_user is None:
        raise HTTPException(status_code=400, detail="Permission denied.")
    
    db_publication = get_publication(db, reservationSchema.publication_id)
    
    if db_publication is None:
       raise HTTPException(status_code=400, detail="Permission denied.")

    if is_the_property_reserved(reservationSchema.start_date, reservationSchema.end_date, db) is True:
        raise HTTPException(status_code=400, detail="The property is reserved.")

    return create_reservation(db_user.id, db_publication.price, reservationSchema, db)

from routes.user_routes import access
from controllers.

@access.post("/publications/", status_code=201)
def create_publication(propertySchema: schemas.PropertySchema, db: Session = Depends(access.get_db)):


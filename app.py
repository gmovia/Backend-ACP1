from fastapi import FastAPI
from routes.review import review
from routes.access import access
from routes.property import propertie
from routes.publication import publication
from routes.user import user
from routes.image import image
from routes.reservation import reservation
from fastapi.middleware.cors import CORSMiddleware


description = """ # API para la gestión de usuarios 👨‍👧‍👧
                """


app = FastAPI(
    description = description,
    title = "Usuarios"
    )

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(access)    
app.include_router(propertie)
app.include_router(publication)
app.include_router(user)
app.include_router(image)
app.include_router(reservation)
app.include_router(review)
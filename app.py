from fastapi import FastAPI
from routes.access import access
from routes.propertyHandler import propertyHandler
from routes.publicationHandler import publicationHandler
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
app.include_router(propertyHandler)
app.include_router(publicationHandler)

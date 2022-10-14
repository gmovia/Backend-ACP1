from fastapi import FastAPI
from routes.access import access
from routes.propertyHandler import propertyHandler

description = """ # API para la gestión de usuarios 👨‍👧‍👧
                """

app = FastAPI(
    description = description,
    title = "Usuarios"
    )

app.include_router(access)    
app.include_router(propertyHandler)

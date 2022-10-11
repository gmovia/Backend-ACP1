from fastapi import FastAPI
from routes.access import access

description = """ # API para la gestión de usuarios 👨‍👧‍👧
                """


app = FastAPI(
    description = description,
    title = "Usuarios"
    )
app.include_router(access)  
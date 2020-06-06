# project/app/main.py
import os

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from app.api import ping

def create_application() -> FastAPI:
    application = FastAPI()

    register_tortoise(
        application,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    application.include_router(ping.router)

    return application


app = create_application()
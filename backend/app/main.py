'''
FastAPI project set up inspired by https://rogulski.it/blog/sqlalchemy-14-async-orm-with-fastapi/
Did strip some elements of the base code
'''
import os
import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.routes.api import api_router
from .core.config import settings

os.environ["TZ"] = settings.TIMEZONE
time.tzset()


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.TITLE,
        description=settings.DESCRIPTION,
        debug=settings.DEBUG
    )
    application.include_router(api_router, prefix=settings.API_V1_STR)
    return application


app = get_application()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8082",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

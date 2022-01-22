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
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        docs_url=f"{settings.API_V1_STR}/docs"
    )
    application.include_router(api_router, prefix=f"{settings.API_V1_STR}")
    return application


app = get_application()


@app.get("/")
async def main():
    return {"Welcome to the api"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

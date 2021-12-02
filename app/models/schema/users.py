from typing import Optional, Any, Dict
from datetime import date, datetime
from uuid import UUID

from pydantic import validator

from app.models.schema.base import BaseSchema


class UserBaseSchema(BaseSchema):
    username: str


class UserBasePW(UserBaseSchema):
    password: str


class UserProfileSchemaIn(UserBasePW):
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[date]


class UserProfileSchema(UserBaseSchema):
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[date]


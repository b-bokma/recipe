import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies.db import get_db
from ..dependencies.functions import get_current_active_user
from ...crud.user import user as cruduser
from ...schemas.users import User, UserCreate

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return User(**current_user.__dict__)


@router.get("/user/{user_id}", status_code=200, response_model=User)  # 1
async def fetch_user(
        *,
        user_id: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_active_user)
) -> Any:
    result = await cruduser.get(db=db, id=user_id)  # 2
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
        )

    return User(**result[0].__dict__)


@router.post("/", response_model=User)
async def create_user(
        *,
        db: AsyncSession = Depends(get_db),
        user_in: UserCreate,
) -> Any:
    user = await cruduser.get_by_email(db, email=user_in.email)

    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = await cruduser.create(db, obj_in=user_in)
    response = User(**user.__dict__)

    return response

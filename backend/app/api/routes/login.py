from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies.db import get_db
from ...core import security
from ...core.config import settings
from ...crud.user import user as crud_user
from ...schemas import token
from ...schemas import users

router = APIRouter()


@router.post("/token", response_model=token.Token)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: AsyncSession = Depends(get_db)
) -> dict:
    """
    Get the JWT for a user with data from OAuth2 request form body.
    """

    user_dict = await crud_user.get_by_email(email=form_data.username, db=db)

    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username")
    user = users.UserInDB(**user_dict.__dict__)

    if not await security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await security.create_access_token(subject=user_dict.id, expires_delta=access_token_expires)

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

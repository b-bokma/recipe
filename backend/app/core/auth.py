from datetime import datetime, timedelta
from typing import Optional, MutableMapping, List, Union

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.ext.asyncio import AsyncSession

from ..api.dependencies.db import get_db
from ..core.config import settings
from ..core.security import verify_password
from ..crud.user import user as crud_user
from ..db.tables.users import User

JWTPayloadMapping = MutableMapping[
    str, Union[datetime, bool, str, List[str], List[int]]
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/token")


async def authenticate(
        *,
        email: str,
        password: str,
        db: AsyncSession = Depends(get_db),
) -> Optional[User]:
    user = await crud_user.get_by_email(email=email, db=db)

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not await verify_password(password, user.hashed_password):  # 1
        raise HTTPException(status_code=400, detail="Incorrect password")

    return user


async def create_access_token(*, sub: str) -> str:  # 2
    return await _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),  # 3
        sub=sub,
    )


async def _create_token(
        token_type: str,
        lifetime: timedelta,
        sub: str,
) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire  # 4
    payload["iat"] = datetime.utcnow()  # 5
    payload["sub"] = str(sub)  # 6

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)  # 8


async def authenticate_user(username: str, password: str, db: AsyncSession = Depends(get_db)):
    user = await crud_user.get_by_email(email=username, db=db)

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

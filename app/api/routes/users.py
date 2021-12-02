import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.users import UserProfileSchema, UserProfileSchemaIn
from app.db.tables.users import Users, UserProfile
router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_200_OK)
async def create_user(user: UserProfileSchemaIn, db: AsyncSession = Depends(get_db)):

    new_user = Users()
    new_user.username = user.username
    new_user.password = user.password
    db.add(new_user)

    r = await db.commit()

    new_user_profile = UserProfile()
    new_user_profile.first_name = user.first_name
    new_user_profile.last_name = user.last_name
    new_user_profile.birth_date = user.birth_date

    db.add(new_user_profile)
    await db.commit()
    return {"status_code":200, "details":"Success"}


@router.get("/", status_code=status.HTTP_200_OK, response_model=UserProfileSchema)
async def retrieve_user(
    username: str, db: AsyncSession = Depends(get_db)
) -> UserProfileSchema:

    user = await db.execute(select(Users).where(Users.username == username))
    user_result = user.scalars().first()

    print(user_result.id)

    user_profile = await db.execute(select(UserProfile).where(UserProfile.user_id == user_result.id))
    user_profile_result = user_profile.scalars().first()

    user_out = UserProfileSchema(
        username=user_result.username,
        first_name=user_profile_result.first_name,
        last_name=user_profile_result.last_name,
        birth_date=user_profile_result.birth_date
    )

    return user_out


from typing import Any, Dict, Optional, Union

from sqlalchemy.ext.asyncio import AsyncSession as Session
from sqlalchemy.future import select

from ..core.security import get_password_hash, verify_password
from ..crud.base import CRUDBase
from ..db.tables.users import User
from ..schemas.users import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    async def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        stmt = select(User).filter(User.email == email)
        result = await db.execute(stmt)
        res = result.scalars().first()

        return res

    async def get_by_id(self, db: Session, *, userid: int) -> Optional[User]:
        stmt = select(User).filter(User.id == userid)
        result = await db.execute(stmt)
        res = result.scalars().first()

        return res

    async def create(self, db: Session, *, obj_in: UserCreate) -> User:

        db_obj = User(
            email=obj_in.email,
            hashed_password=await get_password_hash(obj_in.password)
        )
        db.add(db_obj)

        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    async def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def is_active(self, user: User) -> bool:
        return user.is_active

    async def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)

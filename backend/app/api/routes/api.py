from fastapi import APIRouter, Depends

from . import users, recipes, login
from ..dependencies.functions import get_current_active_user

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(login.router, prefix="/auth", tags=["login"])
api_router.include_router(recipes.router, prefix="/recipes", tags=["recipes"],
                          dependencies=[Depends(get_current_active_user)],
                          )

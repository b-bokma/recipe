import logging
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies.db import get_db
from ...crud.recipe import recipe as crudrecipe
from ...schemas.recipe import Recipe, RecipeCreate, Favorite

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/", status_code=200, response_model=List[Recipe])  # 1
async def fetch_all_recipes(
        *,
        db: AsyncSession = Depends(get_db),
        skip: int = 0,
        limit: int = 100
) -> List[Recipe]:
    """
    Fetch all recipes
    """
    result = await crudrecipe.get_multi(db=db, skip=skip, limit=limit)  # 2
    print(result)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Recipes not found"
        )

    return result


@router.get("/{recipe_id}", status_code=200, response_model=Recipe)  # 1
async def fetch_recipe(
        *,
        recipe_id: int,
        db: AsyncSession = Depends(get_db),
) -> Any:
    """
    Fetch a single recipe by ID
    """
    result = await crudrecipe.get(db=db, id=recipe_id)  # 2
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Recipe with ID {recipe_id} not found"
        )

    return result[0]


@router.post("/", status_code=200, response_model=Recipe)
async def create_recipe(
        *,
        db: AsyncSession = Depends(get_db),
        recipe: RecipeCreate):
    res = await crudrecipe.create(db=db, obj_in=recipe)
    return res


@router.post("/favorite", status_code=200)
async def favorite_recipe(
        favorite: Favorite,
        db: AsyncSession = Depends(get_db)):
    res = await crudrecipe.favorite(db=db, obj_in=favorite)
    return res

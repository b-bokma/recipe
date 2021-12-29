from sqlalchemy.ext.asyncio import AsyncSession as Session

from ..crud.base import CRUDBase
from ..db.tables.recipes import Recipe, Favorites
from ..schemas.recipe import RecipeCreate, RecipeUpdate, Favorite


class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    async def create(self, db: Session, *, obj_in: RecipeCreate) -> Recipe:
        db_obj = Recipe(
            name=obj_in.name,
            summary=obj_in.summary,
            description=obj_in.description,
            submitter_id=obj_in.submitter_id
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def favorite(self, db: Session, *, obj_in: Favorite):
        db_obj = Favorites(
            user_id=obj_in.user_id,
            recipe_id=obj_in.recipe_id
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj


recipe = CRUDRecipe(Recipe)

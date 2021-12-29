from typing import Optional

from pydantic import BaseModel


class RecipeBase(BaseModel):
    name: Optional[str]
    summary: Optional[str]
    description: Optional[str]


class RecipeCreate(RecipeBase):
    submitter_id: int


class RecipeUpdate(RecipeBase):
    pass


# Properties shared by schemas stored in DB
class RecipeInDBBase(RecipeBase):
    id: Optional[int]
    submitter_id: Optional[int]

    class Config:
        orm_mode = True


# Properties to return to client
class Recipe(RecipeInDBBase):
    pass


# Properties properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass


class Favorite(BaseModel):
    user_id: int
    recipe_id: int

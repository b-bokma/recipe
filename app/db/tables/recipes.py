from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import func
from sqlalchemy.orm import relationship


class Recipes(Base):
    __tablename__ = "recipe"

    name = Column(String)
    summary = Column(String)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column('created_by', UUID, ForeignKey('user.id'))
    deleted = Column(Boolean, default=0)

    kitchens = relationship('Kitchens', backref='recipe', lazy='dynamic')
    categories = relationship('RecipeFoodCategory', backref='recipe', lazy='dynamic')


class Kitchens(Base):
    __tablename__ = "kitchen"

    name = Column(String)
    recipe_id = Column(UUID, ForeignKey('recipe.id'))


class Favorites(Base):
    __tablename__ = "recipe_favorites"
    # This is a third association/helper table
    recipe_id = Column('recipe_id', UUID, ForeignKey('recipe.id'))
    user_id = Column('user_id', UUID, ForeignKey('user.id'))


class FoodCategory(Base):
    __tablename__ = "foodcategory"

    name = Column(String)

class RecipeFoodCategory(Base):
    __tablename__ = "recipe_foodcategory"
    # This is a third association/helper table
    recipe_id = Column('recipe_id', UUID, ForeignKey('recipe.id'))
    category_id = Column('category_id', UUID, ForeignKey('foodcategory.id'))


class Courses(Base):
    __tablename__ = "course"

    name = Column(String)

class RecipeCourses(Base):
    __tablename__ = "recipe_course"
    # This is a third association/helper table
    recipe_id = Column('recipe_id', UUID, ForeignKey('recipe.id'))
    course_id = Column('course_id', UUID, ForeignKey('course.id'))


class RecipeNutrition(Base):
    __tablename__ = "recipe_nutrition"
    # This is a third association/helper table
    recipe_id = Column('recipe_id', UUID, ForeignKey('recipe.id'))
    nutrition_id = Column('nutrition_id', UUID, ForeignKey('nutrition.id'))

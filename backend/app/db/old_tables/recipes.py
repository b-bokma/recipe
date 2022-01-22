from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import relationship

from ..base_class import Base


class Recipe(Base):  # 1
    name = Column(String(256), nullable=False)
    summary = Column(String)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    submitter_id = Column(Integer, ForeignKey("user.id"), nullable=True)  # 3
    submitter = relationship("User", back_populates="recipes")
    kitchens = relationship('Kitchens', backref='recipe')
    categories = relationship('RecipeFoodCategory', backref='recipe')


class Kitchens(Base):
    __tablename__ = "kitchen"

    name = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))


class Favorites(Base):
    __tablename__ = "recipe_favorites"
    # This is a third association/helper table
    recipe_id = Column('recipe_id', Integer, ForeignKey('recipe.id'))
    user_id = Column('user_id', Integer, ForeignKey('user.id'))


class FoodCategory(Base):
    __tablename__ = "foodcategory"

    name = Column(String)

class RecipeFoodCategory(Base):
    __tablename__ = "recipe_foodcategory"
    # This is a third association/helper table
    recipe_id = Column('recipe_id', Integer, ForeignKey('recipe.id'))
    category_id = Column('category_id', Integer, ForeignKey('foodcategory.id'))


class Courses(Base):
    __tablename__ = "course"

    name = Column(String)

class RecipeCourses(Base):
    __tablename__ = "recipe_course"
    # This is a third association/helper table
    recipe_id = Column('recipe_id', Integer, ForeignKey('recipe.id'))
    course_id = Column('course_id', Integer, ForeignKey('course.id'))


class RecipeNutrition(Base):
    __tablename__ = "recipe_nutrition"
    # This is a third association/helper table
    recipe_id = Column('recipe_id', Integer, ForeignKey('recipe.id'))
    nutrition_id = Column('nutrition_id', Integer, ForeignKey('nutrition.id'))

from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

class Ingredients(Base):
    __tablename__ = "ingredient"

    name = Column(String)
    allergies = relationship('allergy', backref='ingredients', lazy='dynamic')


class Allergies(Base):
    __tablename__ = "allergy"

    name = Column(String)


class RecipeIngredients(Base):
    __tablename__ = "recipe_ingredients"

    recipe_id = Column('recipe_id', UUID, ForeignKey('recipe.id'))
    recipe = relationship('recipe', backref='owner', lazy='dynamic')

    ingredient_id = Column('ingredient_id', UUID, ForeignKey('ingredient.id'))
    ingredient = relationship(' ingredient', backref='owner', lazy='dynamic')

    measurement_id = Column('measurement_id', UUID, ForeignKey('measurement.id'))
    measurement = relationship(' measurement', backref='owner', lazy='dynamic')

    amount = Column(Float)

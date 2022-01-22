from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from ..base_class import Base


class Ingredient(Base):
    name = Column(String)


class Allergies(Base):
    name = Column(String)
    ingredient_id = Column(Integer, ForeignKey('ingredient.id'))


class RecipeIngredients(Base):
    recipe_id = Column('recipe_id', Integer, ForeignKey('recipe.id'))
    recipe = relationship('Recipe', backref='owner')

    ingredient_id = Column('ingredient_id', Integer, ForeignKey('ingredient.id'))
    ingredient = relationship('Ingredient', backref='owner')

    measurement_id = Column('measurement_id', Integer, ForeignKey('measurement.id'))
    measurement = relationship('Measurements', backref='owner')

    amount = Column(Float)

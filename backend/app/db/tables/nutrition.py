from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base_class import Base


class Nutrition(Base):
    __tablename__ = "nutrition"

    name = Column(String)
    measurement_id = Column('measurement_id', Integer, ForeignKey('measurement.id'))
    measurement = relationship('Measurements', backref='measurement', lazy=True)

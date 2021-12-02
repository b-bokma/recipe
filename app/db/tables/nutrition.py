from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func
from sqlalchemy.orm import relationship


class Nutrition(Base):
    __tablename__ = "nutrition"

    name = Column(String)
    measurement_id = Column('measurement_id', UUID, ForeignKey('measurement.id'))
    measurement = relationship(' measurement', backref='owner', lazy='dynamic')
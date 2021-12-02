from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey, Float
from sqlalchemy import func
from sqlalchemy.orm import relationship


class Measurements(Base):
    __tablename__ = "measurement"

    name = Column(String)
    abbreviation = Column(String)
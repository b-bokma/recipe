from sqlalchemy import Column, String

from ..base_class import Base


class Measurements(Base):
    __tablename__ = "measurement"

    name = Column(String)
    abbreviation = Column(String)

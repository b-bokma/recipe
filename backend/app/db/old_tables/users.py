from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.orm import relationship

from ..base_class import Base


class User(Base):
    first_name = Column(String(256), nullable=True)
    last_name = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    modified_at = Column(DateTime(timezone=True), server_onupdate=func.now(), nullable=True)
    is_superuser = Column(Boolean, default=False)
    recipes = relationship('Recipe', back_populates='submitter')
    hashed_password = Column(String, nullable=False)


class UserTypes(Base):
    __tablename__ = "user_types"

    type_id = Column(Integer, default=1)
    name = Column(String)

from app.db.base_class import Base
from app.db.tables.recipes import Recipes

from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import func
from sqlalchemy.orm import relationship



class Users(Base):
    __tablename__ = "user"

    username = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    modified_at = Column(DateTime(timezone=True), onupdate=func.now())
    type_id = Column(UUID, ForeignKey('user_types.id'))
    deleted = Column(Boolean, default=0)

    favorites = relationship('Recipes', backref='user', lazy='dynamic')


class UserTypes(Base):
    __tablename__ = "user_types"

    type_id = Column(Integer, default=1)
    name = Column(String)
    users = relationship('Users', backref='user_types', lazy='dynamic')


class UserProfile(Base):
    __tablename__ = "user_profile"

    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)

    user_id = Column('user_id', UUID, ForeignKey('user.id'))
    user = relationship('Users', backref='owner')




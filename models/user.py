#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review
import os

class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    storage_type = os.getenv("HBNB_TYPE_STORAGE")

    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
    
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

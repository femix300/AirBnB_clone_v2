#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer

from sqlalchemy.orm import relationship
from os import getenv as gv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    id = Column(String(60), primary_key=True, nullable=False, name="id")
    name = Column(String(128), nullable=False)

    storage_type = gv("HBNB_TYPE_STORAGE")

    # For DBStorage: Relationship with City and cascade delete
    if storage_type == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    if storage_type == 'file':
        @property
        def cities(self):
            """Getter attribute to retrieve linked City instances"""
            from models import storage
            city_instances = storage.all("City")
            return [city for city in city_instances.values()
                    if city.state_id == self.id]

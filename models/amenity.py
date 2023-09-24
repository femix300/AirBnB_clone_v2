#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

# Define a Many-To-Many association table
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Amenity(BaseModel, Base):
    """
    Amenity class for representing amenities in a place.
    """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    places = relationship("Place", secondary=place_amenity,
                          back_populates="amenities")

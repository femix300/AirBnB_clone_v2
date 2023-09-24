#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id',
                             String(60), ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Place class to represent a place available for booking."""
    __tablename__ = 'places'

    city_id = Column(String(60),
                     ForeignKey('cities.id', ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id', ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    city = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")
    reviews = relationship("Review",
                           backref="place",
                           cascade="all, delete-orphan")

    if storage_type == 'db':
        amenities = relationship("Amenity",
                                 secondary=place_amenity, viewonly=False)

    elif storage_type == 'file':
        # Initialize amenity_ids as an empty list
        amenity_ids = []

        @property
        def amenities(self):
            """
            Getter attribute for amenities.
            Returns a list of Amenity instances based on amenity_ids.
            """
            return [models.storage.get("Amenity", amenity_id)
                    for amenity_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            """
            Setter attribute for amenities.
            Appends an Amenity.id to the attribute amenity_ids if.
            """
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)

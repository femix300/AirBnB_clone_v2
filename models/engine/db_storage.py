#!/usr/bin/python3
"""This module defines a class to manage dbstorage for hbnb clone"""

import os
from models.base_model import Base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User



class DBStorage:
    """This class manages storage of hbnb models using Mysqlalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Instatntiates DBStorage"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        d_base = os.getenv("HBNB_MYSQL_DB")
        hbnb_env = os.getenv("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{d_base}',
            pool_pre_ping=True)

        if hbnb_env == "test":
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        obj_list = ['City', 'Amenity', 'User', 'State', 'Place', 'Review']
        objects = []

        if cls is not None:
            objects.extend(self.__session.query(cls).all())  # objects
        else:
            for object in obj_list:
                objects.extend(self.__session.query(object).all())

        dict = {}
        for obj in objects:
            k = f"{obj.__class__.__name__}.{obj.id}"
            dict[k] = obj
        return dict


    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

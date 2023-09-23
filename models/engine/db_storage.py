#!/usr/bin/python3
"""This module defines a class to manage dbstorage for hbnb clone"""

from sqlalchemy import create_engine
from os import getenv as gv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base


class DBStorage:
    """This class manages storage of hbnb models using Mysqlalchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Instatntiates DBStorage"""
        user = gv("HBNB_MYSQL_USER")
        pwd = gv("HBNB_MYSQL_PWD")
        host = gv("HBNB_MYSQL_HOST")
        d_base = gv("HBNB_MYSQL_DB")
        hbnb_env = gv("HBNB_ENV")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{d_base}',
            pool_pre_ping=True)

        if hbnb_env == "test":
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models import base_model

        if cls is None:
            query_objects = []
            for model_class in base_model.Base.__subclasses__():
                query_objects.extend(self.__session.query(model_class).all())
            return {f"{obj.__class__.__name__}.{obj.id}": obj
                    for obj in query_objects}

        if isinstance(cls, str):
            cls = base_model.Base.__subclasses__()[cls]

        return self.__session.query(cls).all()

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

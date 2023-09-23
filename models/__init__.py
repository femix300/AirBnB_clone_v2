#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv as gv

# get the value of the environmental variable
storage_type = gv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

#!/usr/bin/python3
"""Instantiates a storage object"""
from os import getenv

# Determine which storage type to use
storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Always reload existing objects from storage
storage.reload()

#!/usr/bin/python3
"""Instantiates a storage object"""
from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()


if storage.__class__.__name__ == "FileStorage":
    from models.state import State
    if not storage.all(State):
        default_state = State()
        default_state.name = "California"
        storage.new(default_state)
        storage.save()
#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_t
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base if storage_t == "db" else object):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_t == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ""
        state_id = ""

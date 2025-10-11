#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """Representation of a state"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            linked to the current State"""
            from models import storage
            city_list = []
            all_cities = storage.all(City).values()
            for city in all_cities:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

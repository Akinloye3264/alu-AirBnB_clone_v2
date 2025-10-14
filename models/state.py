#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_t

# Conditional inheritance based on storage type
class State(BaseModel, Base if storage_t == "db" else object):
    """ State class """
    __tablename__ = 'states' if storage_t == "db" else None

    if storage_t == "db":
        # Columns for DBStorage
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        # Attributes for FileStorage
        name = ""

        @property
        def cities(self):
            """Getter attribute that returns list of City instances linked to this State"""
            from models.city import City
            from models import storage

            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_t
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base if storage_t == "db" else object):
    """ State class """
    __tablename__ = 'states'
    if storage_t == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """Return list of City instances linked to this State"""
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

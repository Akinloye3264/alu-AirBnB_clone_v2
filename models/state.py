#!/usr/bin/python3
"""Defines the State class"""

from models.base_model import BaseModel
from models.city import City
from models import storage


class State(BaseModel):
    """State class"""
    name = ""

    @property
    def cities(self):
        """Returns the list of City instances with state_id == State.id"""
        city_list = []
        all_cities = storage.all(City).values()
        for city in all_cities:
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

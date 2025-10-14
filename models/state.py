#!/usr/bin/python3
"""Defines the State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    @property
    def cities(self):
        """Returns the list of City instances with state_id == State.id"""
        from models import storage  # ✅ Import inside method to avoid circular import
        from models.city import City

        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

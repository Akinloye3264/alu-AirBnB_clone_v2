#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects or all objects of a class"""
        if cls is not None:
            return {
                key: obj
                for key, obj in self.__objects.items()
                if isinstance(obj, cls)
            }
        return self.__objects

    def new(self, obj):
        """Adds a new object to storage dictionary"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {
            key: value.to_dict()
            for key, value in self.__objects.items()
        }
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value["__class__"]
                    cls = classes.get(cls_name)
                    if cls:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it exists"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Call reload() method for deserializing JSON file to objects"""
        self.reload()

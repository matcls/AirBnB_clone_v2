#!/usr/bin/python3
"""Storage Class for HBnB.
Attributes:
    classes (TYPE): Description
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
           "City": City, "State": State, "Place": Place, "Review": Review}


class FileStorage:
    """Return the dictionary __objects."""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return the dictionary __objects."""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        to_json = {}
        for key in self.__objects:
            to_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(to_json, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, "r") as f:
                for key, value in (json.load(f)).items():
                    self.__objects[key] = classes[value["__class__"]](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """Deserializes the JSON File calling reload method."""
        self.reload()

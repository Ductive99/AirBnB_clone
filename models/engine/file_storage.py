#!/usr/bin/python3
"""
Module that defines the FileStorage class.

-> The class is responsible for serializing instances  to a JSON file,
and deserializing JSON files back to instances.
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json

clss = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}
"""clss (dict): dictionary of class objects"""


class FileStorage:
    """
    Class responsible for handling file storage using JSON.

    Private class attributes:
        - `__file_path` (str): path to the JSON file.
        - `__objects` (dict): empty in the beginning.
            stores all objects by <class name>.id
            (ex: BaseModel object with id=12121212,
                the key will be BaseModel.12121212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the __objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Adds an object to `__objects`.
        with key <class name>.id

        Args:
            obj (object): the object to be added
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """
        Serializes `__objects` to the JSON file
        """
        objs = {}
        for k in self.__objects:
            objs[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(objs, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the file exits).
        Otherwise, nothing is done and no exception is raised.
        """
        try:
            with open(self.__file_path, 'r') as f:
                load = json.load(f)
            for k in load:
                self.__objects[k] = clss[load[k]["__class__"]](**load[k])
        except Exception as e:
            pass

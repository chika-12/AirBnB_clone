#!/usr/bin/python3

import json
import os

"""Creating a base model from another one"""


class FileStorage():
    """Creating the file storage model"""

    __file_path = "file.json"
    __objects = {}  # creating an empty dictionary

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialization of data"""

        serialized_data = {}
        for key, val in self.__objects.items():
            serialized_data[key] = val

        with open(self.__file_path, "w", encoding="UTF-8") as json_file:
            json.dump(serialized_data, json_file, default=str)

    def reload(self):
        """Deserialization of json file if found"""

        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
                return (self.__objects)
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # Do nothing

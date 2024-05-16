import json

"""Creating a base model from another one"""


class FileStorage():
    """Creating the file storage model"""

    def __init__(self, file_path="file.json"):
        """Initializing file storage"""

        self.__file_path = file_path
        self.__objects = {}  # creating an empty dictionary

    def all(self):
        """Returns the dictionary objects"""
        return __objects

    def new(self, obj):
        """Adds a new object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialization of data"""

        with open(self.__file_path, "w", encoding="UTF-8") as json_file:
            json.dumps(self.__objects, json_file)

    def reload(self):
        """Deserialization of json file if found"""

        try:
            with open(self__file.path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass  # Do nothing

import uuid
from datetime import datetime

"""A python model that defines all common attributes/methods for
    other classes
"""


class BaseModel():
    """ Creating base class"""

    def __init__(self, *args, **kwags):
        """Accepts user arguments"""

        if kwags:
            for key, value in kwags.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwags:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwags:
                self.created_at = datetime.now()
            if 'updated_at' not in kwags:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Prints class name, id and a dictionary representation"""

        class_name = self.__class__.__name__
        return f'[<{class_name}>] (<{self.id}>) <{self.__dict__}>'

    def save(self):
        """updates the public instance attribute updated_at with the
            current datetime
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict

import uuid
from datetime import datetime

"""A python model that defines all common attributes/methods for
    other classes
"""


class BaseModel():
    """ Creating base class"""

    def __init__(self, *args, **kwags):
        """Accepts user arguments"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwags.items():
            setattr(self, key, value)

    def __str__(self):
        """Prints class name, id and a dictionary representation"""

        class_name = self.__class__.__name__
        return f'[<{class_name}>] (<{self.id}>) <{self.__dict__}>'

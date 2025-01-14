#!/usr/bin/python3
"""

"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base model class for other classes
    """
    def __init__(self, *args, **kwargs):
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the instance.

        This method creates a copy of the instance's attributes and adds the class name,
        created_at, and updated_at timestamps in ISO format.

        Returns:
        dict: A dictionary representation of the instance.

        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f') #This strftime method converts a datetime object to a string in the specified format.
        #Also, it allows one specify a custom format string.
        instance_dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')

        return instance_dict
    
    def __str__(self):
        """
        Returns a string representation of the instance.

        This method returns a string in the format [class_name] (id) dict,
        where class_name is the name of the class, id is the id of the instance,
        and dict is the dictionary representation of the instance's attributes.
        """
        return "[{class_name}] ({id}) {dict}".format(
            class_name=self.__class__.__name__,
            id=self.id,
            dict=self.__dict__
        )
    

if __name__ == "__main__":

    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        all_obj = FileStorage.__objects
        obj_dict = {}
        for key in all_obj.keys():
            obj_dict[key] = all_obj[key].to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        class_name = eval(class_name)

                        instance = class_name(**value)
                        FileStorage.__objects[key] = instance

                except json.JSONDecodeError:
                    pass

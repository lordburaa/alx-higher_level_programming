#!/usr/bin/python3
"""
    class
"""
import json


class Base:
    """Base Calss """

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:

            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        list_t = []
        str_t = str(list_t)
        if not list_dictionaries:
            return str_t
        elif list_dictionaries is None:
            return str_t
        else:
            json_string = json.dumps(list_dictionaries)
            try:
                lo = json.loads(json_string)
            except json.JSONDecoderError as e:
                return str_t

            return (json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string representatio of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            new = []
        else:
            new = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(Base.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """return of the JSON string representatio json_string"""
        if json_string is None:
            return []
        if not json_string:
            return []
        load_json = json.loads(json_string)
        return load_json

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attribute already set"""
        width = dictionary.get('width', 0)
        height = dictionary.get('height', 0)
        x = dictionary.get('x')
        y = dictionary.get('y')
        up = cls(width, height, x, y)
        up.update(**dictionary)

        return up

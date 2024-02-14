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
            return (json_string)

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

    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

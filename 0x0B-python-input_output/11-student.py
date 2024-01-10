#!/usr/bin/python3
""" creating class """


class Student:
    """student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that returns direcotry description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            new_dict = {}

            for attr in range(len(attrs)):
                for satr in obj:
                    if attrs[attr] == satr:
                        new_dict[satr] = obj[satr]
            return new_dict
        return obj
    

    def reload_from_json(self, json):
            
        return self.update(json)

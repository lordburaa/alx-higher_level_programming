#!/usr/bin/python3
"""
 creating class

"""


class Student:
    """ student class"""
    def __init__(self, first_name, last_name, age):
        """instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retireves a dictionary representatin"""
        dic_t = {}
        if not isinstance(attrs, type(None)):
            for i in attrs:
                try:
                    dic_t[i] = getattr(self, i)
                except AttributeError:
                    pass
            return dic_t
        return self.__dict__

    def reload_from_json(self, json):
        """That replaces all attribute of the Student isinstance:"""

        

#!/usr/bin/python3
"""
    adding attribute
    """


def add_attribute(obj, attr_name, attr_value):
    """
        Args:

            obj: first argumet

            attr_name: second argumet

            attr_value: third argumet
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)

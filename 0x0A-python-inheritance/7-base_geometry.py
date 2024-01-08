#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """base geometry"""
    def area(self):
        """area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

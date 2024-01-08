#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """base geometry"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if self.value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

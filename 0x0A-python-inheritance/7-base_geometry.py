#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """base geometry"""
    def area(self):
        """area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        self.name = name
        self.value = value

        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

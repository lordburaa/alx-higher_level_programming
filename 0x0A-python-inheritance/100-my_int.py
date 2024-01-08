#!/usr/bin/python3
"""creating myInt class"""


class MyInt(int):
    """creating my int class

        checking method """
    def __init__(self, value):
        self.value = value

    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True

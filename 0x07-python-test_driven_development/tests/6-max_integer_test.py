#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class checking the list  to print the max number"""

    def checking_integer(self):
        """checking the function """
        listt = [1 ,2, 3, 6]
        self.assertEqual(max_integer(listt), 6)
        self.assertEqual(max_integer([1,2,3, -1]), 3)

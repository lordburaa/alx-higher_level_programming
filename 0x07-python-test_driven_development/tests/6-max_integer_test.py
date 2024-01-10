#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class checking the list  to print the max number"""
    def test_module_ocstring(self):
            """testing the module docstring"""
            m = __import__('6-max_integer').__doc__
            self.assertTrue(len(m) * 1)
    def checking_list(self):
        """cheking the list"""
        self.assertEqual(max_integer([1,3,4,7]), 7)

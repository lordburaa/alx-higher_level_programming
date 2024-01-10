#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def checking_integer(self):
        listt = [1 ,2, 3, 6]
        self.assertEqual(max_integer(listt), 6)
        self.assertRaises(TypeError, max_integer, [1,2,3,'hello'])

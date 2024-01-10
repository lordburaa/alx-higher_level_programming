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
    def test_listt(self):
        """cheking the list"""
        
        self.assertNotEqual(len([]), 5)

    def test_maxx(self):
        """checking the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_with0(self):
        """cheking with zero"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()

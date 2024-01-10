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
    def test_negative(self):
        """chek=cking the negative number"""
        self.assertEqual(max_integer([-1, -5, -6]), -1)
    def test_positive_negative(self):
        """checking the negative and postive"""
        self.assertEqual(max_integer([-1, 8, -5, -6]), 8) 

    def test_onevalue(self):
        """checking the for one value"""
        self.assertEqual(max_integer([5]), 5)
if __name__ == '__main__':
    unittest.main()

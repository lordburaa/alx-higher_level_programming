"""conatins unittest cases for square class"""
import unittest
from models.base import Base
from models.square import Square



class TestSquare(unittest.TestCase):
    """tests all method and attributes of the squaer
    """
    def test_size(self):
        """tests cerating square with integer size"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_with_zero(self):
        """Test size with zero"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)
            self.assertEqual(e, "width must be > 0")

    def test_size_with_negative(self):
        """test size with negative number"""
        with self.assertRaises(ValueError) as e:
            s1 = Square(-3)
            self.assetEqual(e, "width must be > 0")

    def test_size_string(self):
        """Test size with string"""
        with self.assertRaises(TypeError) as e:
            s1 = Square("5k")
            self.assertEqual(e, "width must be an integer")


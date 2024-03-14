""""conatins test cased of rectange class which extend the base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the rectangel class"""
    def width_height_integer(self):
        """testsfor width and height as integer"""
        Base._Base.__nb_object = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def tesst_with_all_arguments(self):
        """Tests with all vali argumets"""
        Base._Base__nb_object = 0
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_for_private_width(self):
        """testing for width as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__width"))

    def test_for_private_height(self):
        """test for height as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__height"))

    def test_for_private_x(self):
        """Tests for x as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__x"))

    def test_for_private_y(self):
        """Test fro y as private attribute"""
        self.assertFalse(hasattr(Rectangle, "__y"))

    def widht_setter_width_int(self):
        """Test width setter andd getter with integer"""
        Base.__Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        r3.width = 5
        self.assertEqual(r3.width, 5)

    def test_height_setter_getter_with_int(self):
        """test height setter an dgetter with integers"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        r3.height = 5
        self.height =5
        self.assertEqual(r3.height, 5)

    def test_width_setter_getterwith_other_type(self):
        """Test width setter and getter with string"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r3.width = "5"

    def height_setter_getter_with_other_types(self):
        """Test height setter and geter with string"""
        Base._Base_nb_objects = 0
        r3 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r3.height = "5"

    def width_with_string(self):
        """test width with string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle("2", 2)


"""unittest for the base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """handling of base class test cases"""
    def test_with_no_arguments(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_argument(self):
        """test with one object created but with rgument"""
        Base._Base__nb_objects = 0
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_with_and_without_argumet(self):
        """test with multiple object with object with argumetn and one without argumet last"""
        Base._Base__nb_object = 0
        b1 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b5.id, 3)

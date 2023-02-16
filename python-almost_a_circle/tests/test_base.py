#!/usr/bin/python3
from models.base import Base
import unittest


class TestBase(unittest.TestCase):

    def test_simple_using(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)


if __name__ == "__main__":
    unittest.main()

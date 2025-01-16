#!/usr/bin/python3

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test suite for the City class.
    """

    def test_attributes(self):
        """
        Test default values of attributes in City.
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()

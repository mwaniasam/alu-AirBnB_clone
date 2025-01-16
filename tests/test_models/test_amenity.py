#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Test suite for the Amenity class.
    """

    def test_name(self):
        """Test default value of name attribute in Amenity."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()

import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestModels(unittest.TestCase):
    """
    Test suite for models: State, City, Amenity, Place, Review.
    """

    def test_state(self):
        """Test State class"""
        state = State()
        self.assertEqual(state.name, "")

    def test_city(self):
        """Test City class"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_amenity(self):
        """Test Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_place(self):
        """Test Place class"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_review(self):
        """Test Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == "__main__":
    unittest.main()

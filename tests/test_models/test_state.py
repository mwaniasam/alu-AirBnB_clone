#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    Test suite for the State class.
    """

    def test_name(self):
        """Test default value of name attribute in State."""
        state = State()
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()

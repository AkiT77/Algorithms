import unittest
from binary_search import binary_search_function

class TestBinarySearch(unittest.TestCase):
    def test_key_found(self):
        """Test case where the key exists in the array."""
        array = [1, 3, 5, 7, 9, 11]
        key = 7
        result = binary_search_function(array, key)
        self.assertEqual(result, 3)  # Index of 7 in the array

    def test_key_not_found(self):
        """Test case where the key not exists in the array"""
        array = [2, 4, 6, 8, 10]
        key = 7
        result = binary_search_function(array, key)
        self.assertEqual(result, None)  # Index not found

    def test_key_found_at_first_index(self):
        """Test case where the key not exists in the array"""
        array = [2, 4, 6, 8, 10]
        key = 2
        result = binary_search_function(array, key)
        self.assertEqual(result, 0)  # Integer found at first index

    def test_key_found_at_last_index(self):
        """Test case where the key not exists in the array"""
        array = [2, 4, 6, 8, 10]
        key = 10
        result = binary_search_function(array, key)
        self.assertEqual(result, 4)  # Integer found at last index

if __name__ == "__main__":
    unittest.main()
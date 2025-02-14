import unittest
from quickselect import quickselect_function

class TestBinarySearch(unittest.TestCase):
    def test_ascending_order(self):
        """Test case where the array is already sorted in ascending order."""
        array = [1, 3, 5, 7, 9, 11]
        result = quickselect_function(array, 2)
        self.assertEqual(result, 5) 

    def test_descending_order(self):
        """Test case where the array is sorted in descending order."""
        array = [10, 8, 6, 4, 2]
        result = quickselect_function(array, 3)
        self.assertEqual(result, 8)  

    def test_array_with_duplicates(self):
        """Test case with duplicate elements."""
        array = [7, 1, 7, 2, 1, 11]
        result = quickselect_function(array, 3)
        self.assertEqual(result, 7)

if __name__ == "__main__":
    unittest.main()
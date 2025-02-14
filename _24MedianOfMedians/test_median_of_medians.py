import unittest
from median_of_medians import median_of_medians_function

class TestBinarySearch(unittest.TestCase):
    def test_ascending_order(self):
        """Test case where the array is already sorted in ascending order."""
        array = [1, 3, 5, 7, 9, 11]
        result = median_of_medians_function(array)
        self.assertEqual(result, 5) 

    def test_descending_order(self):
        """Test case where the array is sorted in descending order."""
        array = [10, 8, 6, 4, 2]
        result = median_of_medians_function(array)
        self.assertEqual(result, 6)  

    def test_array_with_duplicates(self):
        """Test case with duplicate elements."""
        array = [7, 1, 7, 2, 1, 11]
        result = median_of_medians_function(array)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
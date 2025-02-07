import unittest
from merge_sort import merge_sort_function

class TestBinarySearch(unittest.TestCase):
    def test_ascending_order(self):
        """Test case where the array is already sorted in ascending order."""
        array = [1, 3, 5, 7, 9, 11]
        result = merge_sort_function(array)
        self.assertEqual(result, [1, 3, 5, 7, 9, 11])  # Nothing needs to change

    def test_descending_order(self):
        """Test case where the array is sorted in descending order."""
        array = [10, 8, 6, 4, 2]
        result = merge_sort_function(array)
        self.assertEqual(result, [2, 4, 6, 8, 10])  

    def test_array_with_duplicates(self):
        """Test case with duplicate elements."""
        array = [7, 1, 7, 2, 1, 11]
        result = merge_sort_function(array)
        self.assertEqual(result, [1, 1, 2, 7, 7, 11])
        
    def test_unsorted_array(self):
        """Test case with a randomly ordered array."""
        array = [10, 4, 9, 12, 1, 18]
        result = merge_sort_function(array)
        self.assertEqual(result, [1, 4, 9, 10, 12, 18])

if __name__ == "__main__":
    unittest.main()
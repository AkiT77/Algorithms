import unittest
from select_minimum import select_minimum_function

class TestBinarySearch(unittest.TestCase):
    def test_ascending_order(self):
        """Test case where the array is already sorted in ascending order."""
        array = [502, 25, 63, 0, 78]
        result = select_minimum_function(array)
        self.assertEqual(result, 0)    

    def test_array_with_duplicates(self):
        """Test case with duplicate elements."""
        array = [7, 1, 7, 2, 1, 11]
        result = select_minimum_function(array)
        self.assertEqual(result, 1)

    def test_extra_large_number(self):
        """Test case with extra large numbers."""
        array = [10000, 50854, 6987421, 456213, 99999999]
        result = select_minimum_function(array)
        self.assertEqual(result, 10000)
               
if __name__ == "__main__":
    unittest.main()
import unittest
from select_minimum_and_maximum import select_minimum_and_maximum_function

class TestBinarySearch(unittest.TestCase):
    def test_ascending_order(self):
        """Test case where the array is already sorted in ascending order."""
        array = [502, 25, 63, 0, 78]
        min, max = select_minimum_and_maximum_function(array)
        self.assertEqual(min, 0)    
        self.assertEqual(max, 502) 

    def test_array_with_duplicates(self):
        """Test case with duplicate elements."""
        array = [7, 1, 7, 2, 1, 11]
        min, max = select_minimum_and_maximum_function(array)
        self.assertEqual(min, 1)
        self.assertEqual(max, 11) 

    def test_extra_large_number(self):
        """Test case with extra large numbers."""
        array = [10000, 50854, 6987421, 456213, 99999999]
        min, max = select_minimum_and_maximum_function(array)
        self.assertEqual(min, 10000)
        self.assertEqual(max, 99999999)

    def test_same_number(self):
        """Test case with same numbers."""
        array = [888, 888, 888, 888, 888]
        min, max = select_minimum_and_maximum_function(array)
        self.assertEqual(min, 888)
        self.assertEqual(max, 888)
               
if __name__ == "__main__":
    unittest.main()
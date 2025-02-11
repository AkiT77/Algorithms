import unittest
from hoare_partitioning import hoare_partitioning_function

class TestBinarySearch(unittest.TestCase):
    def test_general_case(self):
        """Test case of general case"""
        array = [7, 3, 9, 4, 7, 5, 7, 8]
        pivot_index = 4
        result = hoare_partitioning_function(array, pivot_index)
        self.assertEqual(result, 5)  

    def test_single_pivot(self):
        """Test case of single pivot"""
        array = [2, 2, 2, 2, 2]
        pivot_index = 2
        result = hoare_partitioning_function(array, pivot_index)
        self.assertEqual(result, 4)  

    def test_no_pivot(self):
        """Test case of no exist pivot"""
        array = [1, 2, 3, 4, 5]
        pivot_index = 6
        result = hoare_partitioning_function(array, pivot_index)
        self.assertEqual(result, None)  

    def test_pivot_largest_element(self):
        """Test case of pivot is the largest element in the array"""
        array = [1, 2, 3, 4, 7]
        pivot_index = 4
        result = hoare_partitioning_function(array, pivot_index)
        self.assertEqual(result, 4)  

if __name__ == "__main__":
    unittest.main()

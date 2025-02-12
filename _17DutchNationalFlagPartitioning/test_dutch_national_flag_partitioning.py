import unittest
from dutch_national_flag_partitioning import dutch_national_flag_partitioning_function

class TestDutchNationalFlagPartitioning(unittest.TestCase):
    def test_general_case(self):
        """Test case of general case"""
        array = [7, 3, 9, 4, 7, 5, 7, 8]
        pivot = 7
        lo, mid = dutch_national_flag_partitioning_function(array, pivot)
        self.assertEqual(lo, 2)  
        self.assertEqual(mid, 5)  

    def test_single_pivot(self):
        """Test case of single pivot"""
        array = [2, 2, 2, 2, 2]
        pivot = 2
        lo, mid = dutch_national_flag_partitioning_function(array, pivot)
        self.assertEqual(lo, -1)  
        self.assertEqual(mid, 4)  

    def test_no_pivot(self):
        """Test case of no exist pivot"""
        array = [1, 2, 3, 4, 5]
        pivot = 3
        lo, mid = dutch_national_flag_partitioning_function(array, pivot)
        self.assertEqual(lo, 1)  
        self.assertEqual(mid, 2)  

    def test_pivot_largest_element(self):
        """Test case of pivot is the largest element in the array"""
        array = [1, 2, 3, 4, 7]
        pivot = 7
        lo, mid = dutch_national_flag_partitioning_function(array, pivot)
        self.assertEqual(lo, 3)  
        self.assertEqual(mid, 4)   

if __name__ == "__main__":
    unittest.main()

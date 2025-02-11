import unittest
from merge import merge_function

class TestBinarySearch(unittest.TestCase):
    def test_one_figure(self):
        """Test case of one figure multiplication"""
        a = [1]
        b = [2]
        result = merge_function(a, b)
        self.assertEqual(result, [1, 2])  

    def test_two_figure(self):
        """Test case of two figure multiplication"""
        a = [1, 2]
        b = [3, 4]
        result = merge_function(a, b)
        self.assertEqual(result, [1, 2, 3, 4])   

    def test_one_pair_same_figure(self):
        """Test case of three figure multiplication"""
        a = [1, 2, 8]
        b = [2, 3, 7]
        result = merge_function(a, b)
        self.assertEqual(result, [1, 2, 2,3, 7, 8])  
        
    def test_two_pair_same_figure(self):
        """Test case of four figure multiplication"""
        a = [1, 5, 8, 9]
        b = [5, 6, 7, 8]
        result = merge_function(a, b)
        self.assertEqual(result, [1, 5, 5, 6, 7, 8, 8, 9])

if __name__ == "__main__":
    unittest.main()
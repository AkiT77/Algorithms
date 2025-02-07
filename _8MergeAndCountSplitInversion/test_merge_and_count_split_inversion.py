import unittest
from merge_and_count_split_inversion import merge_and_count_split_inversion_function

class TestBinarySearch(unittest.TestCase):
    def test_one_figure(self):
        """Test case of one figure multiplication"""
        a = [1]
        b = [2]
        result, inversions = merge_and_count_split_inversion_function(a, b)
        self.assertEqual(result, [1, 2])  
        self.assertEqual(inversions, 0)

    def test_two_figure(self):
        """Test case of two figure multiplication"""
        a = [1, 2]
        b = [3, 4]
        result, inversions = merge_and_count_split_inversion_function(a, b)
        self.assertEqual(result, [1, 2, 3, 4])   
        self.assertEqual(inversions, 0)

    def test_one_pair_same_figure(self):
        """Test case of three figure multiplication"""
        a = [1, 2, 8]
        b = [2, 3, 7]
        result, inversions = merge_and_count_split_inversion_function(a, b)
        self.assertEqual(result, [1, 2, 2, 3, 7, 8])
        self.assertEqual(inversions, 3) #(8, 2), (8, 3), (8, 7)
        
    def test_two_pair_same_figure(self):
        """Test case of four figure multiplication"""
        a = [1, 5, 8, 9]
        b = [5, 6, 7, 8]
        result, inversions = merge_and_count_split_inversion_function(a, b)
        self.assertEqual(result, [1, 5, 5, 6, 7, 8, 8, 9])
        self.assertEqual(inversions, 7) #(8, 5), (8, 6), (8, 7), (9, 5), (9, 6), (9, 7), (9, 8)

if __name__ == "__main__":
    unittest.main()
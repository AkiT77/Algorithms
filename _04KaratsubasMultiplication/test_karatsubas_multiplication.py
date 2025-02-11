import unittest
from karatsubas_multiplication import karatsubas_multiplication_function

class TestBinarySearch(unittest.TestCase):
    def test_one_figure(self):
        """Test case of one figure multiplication"""
        a = 1
        b = 2
        result = karatsubas_multiplication_function(a, b)
        self.assertEqual(result, 2)  

    def test_two_figure(self):
        """Test case of two figure multiplication"""
        a = 12
        b = 34
        result = karatsubas_multiplication_function(a, b)
        self.assertEqual(result, 408)   

    def test_three_figure(self):
        """Test case of three figure multiplication"""
        a = 123
        b = 456
        result = karatsubas_multiplication_function(a, b)
        self.assertEqual(result, 56088)  
        
    def test_four_figure(self):
        """Test case of four figure multiplication"""
        a = 1234
        b = 5678
        result = karatsubas_multiplication_function(a, b)
        self.assertEqual(result, 7006652)

if __name__ == "__main__":
    unittest.main()
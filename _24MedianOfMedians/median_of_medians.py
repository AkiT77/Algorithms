import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _03InsertionSort.insertion_sort import insertion_sort_function
from _23Quickselect.quickselect import quickselect_function
"""
The Median of Medians algorithm is a specialized pivot selection strategy for the Quickselect algorithm.
The Median of medians technique involves finding an approximate median that is sufficient to ensure linear time performance.

The Median of Medians algorithm Steps:
1.  Divide: 
    The original list of n elements is divided into groups of at most 5 elements each.
2.  Median of Groups: 
    Find the median of each group (since they are small, sorting is straightforward).
3.  Recursively Find Median: 
    Use Quickselect to recursively find the median of the medians of these groups.
"""
def median_of_medians_function(array):
    """
    finding an approximate median from an array.

    Parameters:
        array (array[int]): The array that need to be found a approximate median.
        
    Returns:
        int: The value of the median

    Complexity:
        Time Complexity (Best, Worst, Average): O(n)

        Space Complexity:  O(n)
        -   O(n) input space + O(log n) auxiliary space = O(n)
        
        Auxiliary Space:  O(log n)
        -   Due to the recursive calls made during the Quickselect process.
    """
    if len(array) <= 5: 
        return median_of_five(array)
    else:
        medians = []
        for index in range(0, len(array), 5):
            last_index = min(index + 4, len(array) - 1) #To ensure the median array only contain maximum 5 elements
            median = median_of_five(array[index:last_index+1])
            medians.append(median)
        median_index = (len(medians) - 1)//2
        return quickselect_function(medians, (median_index))
    
def median_of_five(array):
    """
    Select the median of an array with a maximum of five element 
    """
    if len(array) == 1:
        return array[0]
    insertion_sort_function(array) #Sort the array with insertion sort function
    return array[len(array) //2] #return the median of the sorted array

# array = [2, 5, 79, 6, 8, 79, 888, 999]
# print(median_of_medians_function(array))
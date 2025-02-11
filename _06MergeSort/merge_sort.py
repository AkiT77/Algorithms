import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _5Merge.merge import merge_function
"""
Merge Sort is a divide and conquer algorithm. 
Merge Sort Steps:
1.  It recursively divides the array into halves until each subarray contains only one element. (len(array) > 1)
2.  Then, it uses the merge algorithm to 'conquer'(combine) these smaller subarrays back together in sorted order recursively.
"""
def merge_sort_function(array):
    """
    Sorts the array in ascending order using the merge sort algorithm.
   
    Args:
        array (list[int]): A list of integer to sort.

    Returns:
        array (list[int]): The sorted array.
    
    Complexity:
        Time Complexity: O(N log N)
        - Since there are log N levels and each level requires O(N) work to merge the subarrays

        Space Complexity: O(N) 
        - input space + auxiliary space = O(N) + O(N) = O(N)
        
        Auxiliary Space: O(N) 
        - In each recursive call, new arrays are created to store the merged results temporarily

    """
    if len(array) > 1:
        mid = len(array) // 2
        array[:mid] = merge_sort_function(array[:mid])  
        array[mid:] = merge_sort_function(array[mid:])  
        array = merge_function(array[:mid], array[mid:])  
    return array

a = [1,5,3,2,8]
print(merge_sort_function(a))
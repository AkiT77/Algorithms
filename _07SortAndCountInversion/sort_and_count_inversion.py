import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _08MergeAndCountSplitInversion.merge_and_count_split_inversion import merge_and_count_split_inversion_function

"""
Sort and count split inversion function is an extension of the merge sort algorithm.
In addition to sorting array, it also counts the number of inversion pairs during the 'divide process'
The code concept is same as the merge sort algorithm, please refer to the explanation of the merge sort algorithm.
"""

def sort_and_count_inversion_function(array):
    """
    Sorts the array in ascending order using the sort and count inversion algorithm, and retrieve the number of inversion pairs.
   
    Args:
        array (list[int]): A list of integer to sort.

    Returns:
        tuple(array (list[int]), int): 
        -   array (list[int]): A list of integer to sort.
        -   int: number of inversion pair
    
    Complexity:
        Time Complexity: O(N log N)
        - Since there are log N levels and each level requires O(N) work to merge the subarrays.

        Space Complexity: O(N) 
        - input space + auxiliary space = O(N) + O(N) = O(N)
        
        Auxiliary Space: O(N) 
        - In each recursive call, new arrays are created to store the merged results temporarily.

    """
    if len(array) == 1:
        return ([array[0]], 0)
    else:
        mid = len(array) // 2
        (array[:mid], InvL) = sort_and_count_inversion_function(array[:mid])
        (array[mid:], InvH) = sort_and_count_inversion_function(array[mid:])
        (new_array, InvS) = merge_and_count_split_inversion_function(array[:mid], array[mid:])
        Inv = InvL + InvH + InvS
        return (new_array, Inv)

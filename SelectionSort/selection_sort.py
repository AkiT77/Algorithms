"""
Selection Sort Steps
1.  Consider the array as two parts: Sorted(initially empty) and Unsorted(initially the entire array).
2.  Starting from the first unsorted number in the array, find the smallest number in the unsorted part.
3.  Swap it with the first unsorted number, and repeat the process until the entire array is sorted.
"""
def selection_sort_function(array):
    """
    Sorts the array in ascending order using the selection sort algorithm.
   
    Args:
        array (list[int]): A list of integer to sort.

    Returns:
        array (list[int]): The sorted array.
    
    Complexity:
        Time Complexity: O(N^2) 
        since the array is halved at each step

        Space Complexity: O(N) 
        - input space + auxiliary space = O(N) + O(1) = O(N)
        
        Auxiliary Space: O(1) 
        - Constant space needed

    """
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
         if array[j] < array[min]:
            min = j
        array[i], array[min] = array[min], array[i]
    return array
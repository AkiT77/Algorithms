"""
Insertion Sort Steps
1.  Consider the array as two parts: Sorted (initially containing only the first element) and Unsorted (initially containing the rest of the array).
2.  Starting from the first number in the Unsorted portion, compare it with the numbers in the Sorted portion (to its left).
3.  Shift larger numbers in the Sorted portion one position to the right until you find the correct position for the current number. 
    Insert the number into its correct position.
4.  Repeat this process for every number in the Unsorted portion until the entire array is sorted.
"""
def insertion_sort_function(array):
    """
    Sorts the array in ascending order using the insertion sort algorithm.
   
    Args:
        array (list[int]): A list of integer to sort.

    Returns:
        array (list[int]): The sorted array.
    
    Complexity:
        Time Complexity: 
            Best case: O(N)
            - When the input array is already sorted.
            Worst case: O(N^2) 
            - When the input array is already sorted.
            Average case: O(N^2) 

        Space Complexity: O(N) 
        - input space + auxiliary space = O(N) + O(1) = O(N)
        
        Auxiliary Space: O(1) 
        - Constant space needed

    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while(j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    return array
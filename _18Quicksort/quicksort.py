import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _16HoarePartitioning.hoare_partitioning import hoare_partitioning_function
"""
For Quicksort algorithm:
1.  Pivot Selection: Choose the first element as the pivot.
2.  Partitioning: Use the Hoare partitioning algorithm to find the correct index of the pivot. 
    (Alternatively, other partitioning algorithms such as Naive partitioning or Dutch National Flag partitioning can be used.)
3.  Recursion: Recursively call the Quicksort function on the two halves of the array based on the pivot.

Note: The implementation can be optimized to reduce the auxiliary space complexity to O(log n).
"""
def quicksort_function(array):
    """
    Sort the array using Hoare Partitioning.

    Parameters:
        array (array[int]): The array that need to be sorted

    Returns:
        array (array[int]): The sorted array.

    Complexity:
        Time Complexity: 
        -   Base case: O(nlog(n))
            The pivot turns out to be the median of the array.
            At each level, the partitioning takes O(n) total time, 
            and only having log2(n) levels of recursion since the size of the array would be halved at
            each level.
        
        -   Worst case: O(n^2)
            The pivot element might be the smallest or largest element of the array.
            At each level, the partitioning takes O(n) total time, 
            and the size of the subproblems solved recursively will be 0 and n - 1(suppose the pivot is the smallest element in the array).

        - Average case: O(nlog(n))

        Total Space Complexity: O(N)  
        -   Input space + auxiliary space = O(N) + O(1)
        
        Auxiliary Space: O(n) 
        -   O(n) for the call stack + O(n) for array slicing = O(n)
    """
    if len(array) <= 1:
        return array
    
    lo = 0
    hi = len(array) - 1
    if hi > lo:
        mid = hoare_partitioning_function(array, lo)
        array[lo:mid] = quicksort_function(array[lo:mid])
        array[mid + 1:hi+1] = quicksort_function(array[mid + 1:hi+1])
    return array

array = [7, 3, 9, 4, 7, 5, 7, 8]
print(quicksort_function(array))
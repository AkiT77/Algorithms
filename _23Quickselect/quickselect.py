import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _16HoarePartitioning.hoare_partitioning import hoare_partitioning_function
"""
1.  The Quickselect algorithm is based on the Quicksort algorithm.
2.  It is based on the observation that if we use Quicksort to find the kth order statistic,
    then at every level of recursion, sorting the half of the array that does not contain the answer is
    unnecessary, and can therefore be skipped. 
3.  In Quickselect, after each partitioning step, only one subarray is chosen for further partitioning, resulting in just one recursive call per step.
"""
def quickselect_function(array, k):
    """
    Quickselect identifies the k-th smallest element by using Hoare partitioning algorithm.

    Parameters:
        array (array[int]): The array from which to get the element.
        k (int): The k-th smallest element in an array we want to find

    Returns:
        int: The value of the element in the array that we want to retrieve.

    Complexity:
        Time Complexity: 
        -   Base case: O(n)
            The total time complexity is the sum of the partitioning steps.
            For example: T(n) = n + n/2 + n/4 + n/8
            This series is a geometric series that sums to O(2n), which is O(n).
        
        -   Worst case: O(n^2)
            might select the minimum or maximum element as the pivot and hence perform O(n) levels of recursion
        
        -   Average case: O(n)
            each partitioning step reduces the problem size by half.

        Total Space Complexity: O(N)  
        -   Input space + auxiliary space = O(N) + O(1)
        
        Auxiliary Space: O(log n)
        -   the depth of the recursion tree is O(log n) because each partitioning step reduces the problem size approximately in half.
    """
    lo = 0
    hi = len(array) - 1
    if hi > lo:
        mid = hoare_partitioning_function(array, lo)
        if k < mid:
            return quickselect_function(array[lo:mid], k)
        elif k > mid:
            return quickselect_function(array[mid+1:], k - len(array[lo:mid+1]))
        else:
            return array[k]
    else:
        return array[k]
    
# array = [2, 5, 8, 9, 2, 18]
# value = quickselect_function(array, 2)
# print(value)

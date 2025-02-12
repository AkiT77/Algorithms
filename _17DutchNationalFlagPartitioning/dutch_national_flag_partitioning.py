"""
Given an array of n objects (array[1..n]) coloured red, white or blue, sort them so that
all objects of the same colour are together, with the colours in the order red, white and
blue.
Maintain three pointers lo, mid, hi such that:
-   array[1..lo - 1] contains the red items
-   array[lo..mid -  1] contains the white items
-   array[mid..hi] contains the currently unknown items
-   array[hi+1..n] contains the blue items
"""
def dutch_national_flag_partitioning_function(array, pivot):
    """
    Used to rearranged the element in the array to store the element which smaller then the pivot to its left,
    and larger to its right,
    and return the index of the pivot

    Parameters:
        array (array[int]): The array that need to be sorted
        pivot (int): The index of the element chosen as the pivot (note: pivot value is at array[pivot]).
       
    Returns:
        int: The index where elements less than the pivot end.
        int: The index where elements is the last element which is equal to the pivot


    Complexity:
        Time Complexity: O(N)   
        -   The algorithm processes each element in the array exactly once.

        Total Space Complexity: O(N)  
        -   Input space + auxiliary space = O(N) + O(1)
        
        Auxiliary Space: O(1) 
        -   In place, no extra space is used
    """
    lo = 0 #Tracks the boundary for elements less than the pivot.
    mid = 0 #Scans through the array.
    hi = len(array) - 1 #Tracks the boundary for elements greater than the pivot.

    while mid <= hi:
        if array[mid] < pivot:
            array[mid], array[lo] = array[lo], array[mid]
            lo += 1
            mid += 1
        elif array[mid] == pivot:
            mid += 1
        else:
            array[mid], array[hi] = array[hi], array[mid]
            hi -= 1
    return lo-1, mid-1
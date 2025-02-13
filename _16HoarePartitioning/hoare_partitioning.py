"""
1.  The Hoare partitioning scheme assumes the pivot is the first element of the range. 
2.  A key drawback of this approach, compared to the naive partitioning scheme, is that it is unstable.
3.  A major downside of the Hoare partitioning scheme, as described above, 
    is its poor performance when there are many elements equal to the pivot.

Hoare partitioning Steps:
1.  In the while loop:
    a.  Move the i pointer to the right until we find an element larger than the pivot.
    b.  Move the j pointer to the left until we find an element smaller than the pivot.
    c.  Swap the elements at i and j if i <= j
        -   This ensures that all elements smaller than the pivot are on the left side, 
            and elements larger than the pivot are on the right side.
        -   The loop continues until i surpasses j.
        -   Important note: 
            On the last iteration of the outer while loop, 
            i will become greater or equal than j, meaning the condition i <= j will no longer be true, 
            and we stop. At this point, the j pointer will be pointing to the last element that is smaller than the pivot.
2.  Swap the pivot:
    -   After exiting the loop, swap the pivot (which was initially at index 0) with the element at index j.
    -   The index j now represents the position of the pivot after partitioning.
"""
def hoare_partitioning_function(array, pivot_index):
    """
    Used to rearranged the element in the array to store the element which smaller then the pivot to its left,
    and larger to its right,
    and return the index of the pivot

    Parameters:
        array (array[int]): The array that need to be sorted
        pivot (int): The index of the element chosen as the pivot (note: pivot value is at array[pivot]).
       
    Returns:
        int: the position of the pivot

    Complexity:
        Time Complexity: O(N)   
        -   The algorithm processes each element in the array exactly once.

        Total Space Complexity: O(N)  
        -   Input space + auxiliary space = O(N) + O(1)
        
        Auxiliary Space: O(1) 
        -   In place, no extra space is used
    """
    pivot = array[pivot_index]
    array[0], array[pivot_index] = array[pivot_index], array[0] #Move the pivot to the front of the array
    i = 0
    j = len(array) - 1
    while i <= j:
        # Move i right until we find an element larger than the pivot
        while i <= j and array[i] <= array[0]:
            i = i + 1
        # Move j left until we find an element smaller than the pivot
        while i <= j and array[j] > array[0]:
            j = j - 1
        #Swap elements if i is still less than or equal to j
        if i <= j:
            array[i], array[j] = array[j], array[i] #swap elements on the wrong side

    array[0], array[j] = array[j], array[0] #swap the pivot into the correct position 
    return j #Return the position of the pivot


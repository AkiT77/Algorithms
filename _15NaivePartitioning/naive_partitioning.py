"""
 The naive partitioning algorithm simply partitions the array into three temporary arrays:
    1.  less than the pivot
    2.  greater than the pivot
    3.  equal to the pivot
"""
def naive_partitioning_function(array, pivot):
    """
    Used to rearranged the element in the array to store the element which smaller then the pivot to its left,
    and larger to its right,
    and return the index of the pivot

    Parameters:
        array (array[int]): The array that need to be sorted
       
    Returns:
        -

    Complexity:
        Time Complexity: O(N)   

        Total Space Complexity: O(N)  
        
        Auxiliary Space: O(N) 
        -   It stores all n elements in new arrays, using O(n) space
    """
    left = [] # Store elements less than the pivot
    pivots = [] # Store elements equal to the pivot
    right = [] # Store elements greater than the pivot

    for i in range(len(array)):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] == pivot:
            pivots.append(array[i])

        else:
            right.append(array[i])

    array = left + pivots + right # Concatenate the arrays
    if len(pivots) == 0:
        return 0
    return len(left) + len(pivots) // 2     # Return the position of the middle pivot 

# Example array and pivot
array = [7, 3, 9, 4, 7, 5, 7, 8]
pivot = 7
result = naive_partitioning_function(array, pivot)
print("Partition result:", result)   
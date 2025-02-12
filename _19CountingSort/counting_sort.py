"""
1.  All elements are integers in the range 0 to u - 1.
"""
def counting_sort_function(array, u):
    """
    Sort the array.

    Parameters:
        array (array[int]): The array that need to be sorted
        u (int): The largest element in the array plus 1.

    Returns:
        array (array[int]): The sorted array.

    Complexity:
        Time Complexity: O(n + u)
        -    Counting sort takes linear time in n if and only if u = O(n). 
        -   O(u) (Initialization of Counter Array) + O(n) (Counting Occurrences) + O(u) (Calculation of Positions) +
            O(n) (Placement into Temporary Array) + O(n) (Copying Sorted Values Back)
        
        Total Space Complexity: O(n + u)
        
        Auxiliary Space: O(n + u)
        -   O(n) for the temp array + O(u) for the counter and position arrays
    """
    # Initialize counter array to store the number of occurrences of each number
    counter = [0] * u
    
    # Count occurrences of each value
    for num in array:
        counter[num] += 1
    
    # Initialize position array to store the starting index of the corresponding number 
    position = [0] * u
    
    # Compute positions
    # Starting from 0, because 0 will always start at index 0.
    for v in range(1, u):
        position[v] = position[v - 1] + counter[v - 1]
    
    # Create temp array to store the sorted result
    temp = [0] * len(array)
    
    # Place values into the correct positions
    for num in array:
        temp[position[num]] = num
        position[num] += 1
    
    # Copy sorted values back into the input array
    for i in range(len(array)):
        array[i] = temp[i]
    
    return array


array = [3, 8, 4, 5, 7, 6, 1, 1, 0, 2, 2]
u = max(array) + 1 
counting_sort_function(array, u)
print("Sorted array:", array)

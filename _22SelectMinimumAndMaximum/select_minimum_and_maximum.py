"""
Select minimum and maximum is a function to find both the maximum and minimum numbers in an array,
follows the same principle as select minimum algorithm. 
The only difference is that it also identifies the maximum value at the same time.
"""
def select_minimum_and_maximum_function(array):
    """
    Select the minimum and maximum element in the array.

    Parameters:
        array (array[int]): The array that need to be sorted
        
    Returns:
        int: The minimum number in the array.
        int: The maximum number in the array.

    Complexity:
        Time Complexity(Best, Worst, Average Case): O(n)
        -   n is the number of elements in the array
        
        Total Space Complexity:  O(n)
        -   input space + auxiliary space = O(n) + O(1)
        
        Auxiliary Space:  O(1)
        -   In-place
    """
    min = array[0]
    max = array[0]
    index = len(array) % 2
    # start at 1 if n is even, 2 if n is odd
    # To ensure that every i + 1 is within the index bounds
    for i in range(index, len(array) - 1): 
        if array[i] < array[i + 1]:
            if array[i] < min:
                min = array[i]
            if array[i + 1] > max:
                max = array[i + 1]
        else:
            if array[i] > max:
                max = array[i]
            if array[i + 1] < min:
                min+ array[i + 1]

    return min, max

array = [1, 0, 99, 875, 45]
min, max = select_minimum_and_maximum_function(array)
print(min,max)
        
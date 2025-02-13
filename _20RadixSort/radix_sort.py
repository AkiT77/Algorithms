"""
Radix Sort
1.  Radix Sort is similar to Counting Sort but it sorts numbers based on individual digits.
    It processes each digit, from the least significant digit (LSD) to the most significant digit (MSD), 
    or vice versa, depending on the implementation.

Note: 
    Radix Sort is useful for sorting large arrays where the number of digits in the largest number 
    is small relative to the number of elements. 
    Counting Sort, on the other hand, is effective for sorting arrays with a limited range of integers.
"""

def radix_sort_function(array, base, digits):
    """
    Sort the array.

    Parameters:
        array (array[int]): The array that need to be sorted
        base: The base of the number system, such as 10 for decimal or 2 for binary.
        digits: How many digits there are in the largest number

    Returns:
        array (array[int]): The sorted array.

    Complexity:
        Time Complexity(Best, Worst, Average Case): O(d(n + b)) 
        -   d is the number of digits
        -   n is the number of elements
        -   b is the base of the number system
        
        Total Space Complexity:  O(n + b)
        
        Auxiliary Space:  O(n + b)
        -   a temporary array for radix pass
    """
    for digit in range(digits):
        radix_pass(array, base, digit)
    return array

def radix_pass(array, base, digit):
    """
    Sort the element in the array base on the specific base and the digit.

    Parameters:
        array (array[int]): The array that need to be sorted
        base (int): The base of the number system, such as 10 for decimal or 2 for binary.
        digit (int): The digit in the digits

    Returns:
        array (array[int]): The sorted array base on the base.

    Complexity:
        Time Complexity: O(n + b)
        -   n is the number of elements
        -   b is the base of the number system

        Total Space Complexity: O(n + b)
        
        Auxiliary Space: O(n + b)

    """
    # Initialize the counter array
    counter = [0] * base
    
    # Count occurrences of each digit at the specified position
    for i in range(len(array)):
        digit_value = get_digit(array[i], base, digit)
        counter[digit_value] += 1 
    
    # Initialize the position array, to keeps track of where each digit should go in the sorted array.
    position = [0] * base  
    
    # Calculate positions
    for v in range(1, base):  # for v = 1 to base-1 do
        position[v] = position[v - 1] + counter[v - 1] 
    
    # Create temp array to store the sorted result
    temp = [0] * len(array) 
    
    # Place values into the correct positions
    for i in range(len(array)):  
        digit_value = get_digit(array[i], base, digit)
        temp[position[digit_value]] = array[i]  
        position[digit_value] += 1 
    
    # Copy the sorted values back to the original array
    for i in range(len(array)): 
        array[i] = temp[i]

def get_digit(number, base, digit):
    # A utility function to extract the digit at a given position
    return (number // base ** digit) % base


array = [170, 45, 75, 90, 802, 24, 2, 66]
base = 10
digits = 3 
radix_sort_function(array, base, digits)
print(array)
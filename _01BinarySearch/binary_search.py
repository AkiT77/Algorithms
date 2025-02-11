def binary_search_function(array, key):
    """
    Performs a binary search to find the index of a key in a sorted array.

    Args:
        array (list[int]): A sorted list of numbers to search.
        key (int): The number to find in the array.

    Returns:
        int: The index of the key in the array, if found.
        None: If the key does not exist in the array.
    
    Complexity:
        Time Complexity: O(log n) 
        -   since the array is halved at each step

        Space Complexity: O(N) 
        -   input space + auxiliary space = O(N) + O(1) = O(N)
        
        Auxiliary Space: O(1) 
        -   constant space
    """
    lo = 0 
    hi = len(array) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        print(f"Current state: lo={lo}, hi={hi}, mid={mid}, array[mid]={array[mid]}")
        if array[mid] == key:  # Key found
            return mid
        elif key > array[mid]:
            print(f"Key {key} > array[mid] ({array[mid]}): Updating lo from {lo} to {mid+1}")
            lo = mid + 1 
        else:
            print(f"Key {key} < array[mid] ({array[mid]}): Updating hi from {hi} to {mid-1}")
            hi = mid - 1

    if array[lo] == key:
        return lo
    else:
        return None

array = [1, 3, 5, 7, 9, 11]
key = 11
print(binary_search_function(array, key))

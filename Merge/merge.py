"""
Merge algorithm Step:
1.  Check if either array has been fully processed:
        First, check if the pointers i and j are within the valid range for their respective arrays (A and B).
        If both pointers are out of bounds, then return the result array.
2.  Merging:
    If either pointer (i or j) is still within the bounds of the respective array, check the following conditions:
        If the second array (B) is fully appended (j > n2), then the remaining elements in A will be appended to the result array.
        If the first array (A) is not fully appended (i <= n1), and A[i] <= B[j], then append the element from A to the result array.
        Else, append the element from B to the result array.
3.  Repeat:
    Continue this process until all elements from both arrays are appended to the result (i <= n1 or j <= n2, all False).

"""
def merge_function(A, B):
    """
    Merge two sorted array into ascending order

    Parameters:
        A (int): The first sorted array.
        B (int): The second sorted array.
    
    Returns:
        array[int]: A new sorted array that contains all elements from both arrays A and B.

    Complexity:
        Time Complexity: O(n + m) 
        n : length of array A
        m : length of array B
        The total number of comparisons is proportional to the total number of elements, which is n+m.

        Total Space Complexity: O(n + m)  
        input space + auxiliary space = O(n + m) + O(n + m) = O(n + m) 
        
        Auxiliary Space: O(n + m) 
        Need extra space to store the merged result array
    """
    result = []
    i = 0
    j = 0
    n1 = len(A) - 1
    n2 = len(B) - 1
    while i <= n1 or j <= n2:
        if j > n2 or (i <= n1 and A[i] <= B[j]):
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    return result

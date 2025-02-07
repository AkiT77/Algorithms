"""
Merge and count split inversion function is an extension of the merge algorithm.
In addition to merging two sorted arrays, it also counts the number of inversion pairs
that occur between the two arrays during the merge process.

What is an Inversion Pair?

Consider the array:
    C = [2, 4, 8, 3, 4, 5]

In this example:
    - (4, 3), (8, 3), (8, 4), and (8, 5) are inversion pairs.

However, in the "Merge and Count Split Inversion" function, inversion pairs are treated slightly differently:
    -   The "Sort and Count Inversion" algorithm, which utilizes the "Merge and Count Split Inversion" function, 
        works recursively by dividing the array into halves during the merge process.
    -   Even though the array is split into two sub-arrays, 
        we treat them as part of the whole array and apply a more efficient method to count inversions during the merge step.

In the "Merge and Count Split Inversion" function, an inversion pair is defined as:
    - A pair of elements where:
        1. One element is larger than the other.
        2. The larger element appears before the smaller element when merging the two sorted sub-arrays.

For example:
    A = [2, 4, 8]
    B = [3, 4, 5]

In this case:
    - (4, 3) is an inversion pair because 4 from array A is larger than 3 from array B.
    - (8, 3), (8, 4), and (8, 5) are also inversion pairs because 8 from array A is larger than these elements from array B.

Key Insight for Counting Inversions:
    Whenever an element in array A is greater than an element in array B during the merge process,
    all the remaining elements in array A (after the current element) will also form inversion pairs 
    with the current element from array B. This insight helps in counting inversions efficiently.

Calculation of Inversions:
The inversion count is updated as follows:
splitInversions += (n1 + 1) - i
Where:
    - n1 is the length of array A.
    - i is the current index in array A being processed.
    - n1 + 1 represents the total number of elements in array A.
    - Subtracting i ensures that we count only those elements in A that are yet to be processed 
      and that are larger than the current element in B.
"""

def merge_and_count_split_inversion_function(A, B):
    """
    Merge two sorted array into ascending order and return the number of inversions

    Parameters:
        A (int): The first sorted array.
        B (int): The second sorted array.
    
    Returns:
        tuple(array[int], int): 
        - array[int]: A new sorted array that contains all elements from both arrays A and B.
        - int: the number of inversions

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
    splitInversions = 0
    i = j = 0
    n1 = len(A) - 1
    n2 = len(B) - 1

    while i <= n1 or j <=n2:
        if j > n2 or(i <= n1 and A[i] <= B[j]):
            result.append(A[i])
            i +=1
        else:
            result.append(B[j])
            j +=1
            splitInversions = splitInversions + (n1 + 1) - i
    return (result, splitInversions)

A = [2, 4, 6]
B = [1, 3, 5]
merged, inversions = merge_and_count_split_inversion_function(A, B)
print("array:", merged)
print("number of inversions pair:", inversions)
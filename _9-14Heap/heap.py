"""
Heap structure here, the first element in the heap will be in the index 1 of the array
The heap will have a maximum logN height. 
Every element in a max heap is no smaller than its children
"""
class MaxHeap:
    array = []
    max_size = 0
    heap_size = 0

    def __init__(self, max_size):
        self.max_size = max_size
        self.array = [None] *(max_size + 1) #1 based index
        self.heap_size = 0
    
    def heapify(self):
        """
        Convert a given (not necessarily sorted) array into a min/max heap
        
        Parameters:
            array (array[int]): The array that represents the heap.

        Returns:
            -

        Complexity:
            Time Complexity: 
            -Best case: O(N)
                If the heap is already balanced after converting the array into a max heap.
                The for loop will run for N/2 times.
            - Worst case: O(N log N) 
                If the array is in ascending order, 
                each node may need to fall all the way down to the bottom of the heap, 
                which fall function takes O(log N) time for each loops. (N/2)
            - Average case: O(N log N)
                On average, the node will need to be moved down through a portion of the heap, 
                so the complexity remains O(N log N).


            Total Space Complexity: O(N)  
            input space + auxiliary space = O(N) + O(1) = O(N) 
            
            Auxiliary Space: O(1) 
            No extra space is used
        """
        # Start from the last parent to the root
        # n // 2 is the index of last non leaf node
        for i in range (self.heap_size // 2, 0, -1):
            self.fall(i)
            

    def insert(self, array, x):
        """
        insert an element into the heap, and ensuring the heap property is maintained.
        
        Parameters:
            array (array[int]): The array that represents the heap.
            x (int): Element to be added to the heap.

        Returns:
            -

        Complexity:
            Time Complexity: 
            -Best case: O(1)
                If the heap is already balanced after adding the element to the heap
            - Worst case: O(log N) 
                The element need to be added is the maximum element in the heap
                After adding the element, we may need to rise the new element up to the heap (using the rise function). 
                This operation requires O(log N) comparisons and swaps.
            - Average case: O(log N)
                On average, the node will need to be moved up through a portion of the heap, 
                so the complexity remains O(log N).


            Total Space Complexity: O(N)  
            input space + auxiliary space = O(N) + O(1) = O(N) 
            
            Auxiliary Space: O(1) 
            No extra space is used
        """
        if self.heap_size >= self.max_size:
            print("Heap is full")
            return
        self.array.append(x)
        self.heap_size += 1
        self.rise(self.heap_size)

    def delete(self): #extract_max
        """
        Get the maximum element from the heap and remove it, ensuring the heap property is maintained.
        
        Parameters:
            -

        Returns:
            int: The maximum element of the heap

        Complexity:
            Time Complexity: 
            -Best case: O(1)
                If the heap is already balanced after extract the maximum element from the heap
            - Worst case: O(log N) 
                After swapping the root with the last element, we may need to "sink" the new root down the heap (using the fall function). 
                This operation requires O(log N) comparisons and swaps.
            - Average case: O(log N)
                On average, the node will need to be moved down through a portion of the heap, 
                so the complexity remains O(log N).


            Total Space Complexity: O(N)  
            input space + auxiliary space = O(N) + O(1) = O(N) 
            
            Auxiliary Space: O(1) 
            No extra space is used
        """
        if self.heap_size == 0:
            print("Heap is empty!")
            return None
        
        n = len(self.array) - 1
        # Swap the root(max) with the last element
        self.array[1], self.array[n] = self.array[n],self.array[1]
        self.heap_size -= 1
        #Get the max element and remove it
        max_value = self.array.pop_back()
        # Restore the max heap property by calling the fall function on the root
        self.fall(1)

        return max_value

    def rise(self, i):
        """
        Move an element higher up to its correct position to maintain the heap property.

        Parameters:
            array (array[int]): The array that represents the heap.
            i (int): The index of the node (parent node) that needs to be rise to maintain the heap property.
        
        Returns:
            -

        Complexity:
            Time Complexity: 
            -Best case: O(1)
                The node is already in the correct position
            - Worst case: O(log N) 
                The node may need to be raised all the way to the top of the heap, requiring O(log N) comparisons and swaps.
            - Average case: O(log N)
                On average, the node will need to be moved up through a small portion of the heap, so the complexity remains O(log N).


            Total Space Complexity: O(N)  
            input space + auxiliary space = O(N) + O(1) = O(N) 
            
            Auxiliary Space: O(1) 
            No need extra space to store 
        """
        parent = i // 2
        # Check if the parent exists
        while parent >= 1:
            if self.array[parent] < self.array[i]:
                self.array[parent], self.array[i] = self.array[i], self.array[parent]
                i = parent
                parent = i//2
            else:
                break

    def fall(self, i):
        """
        Move an element at index i down down the heap to maintain the heap property.

        Parameters:
            array (array[int]): The array that represents the heap.
            i (int): The index of the node (parent node) that needs to be "sunk down" to maintain the heap property.
        
        Returns:
            -

        Complexity:
            Time Complexity: 
            -Best case: O(1)
                The node is already in the correct position
            - Worst case: O(N log N) 
                The node may need to be "sunk" all the way to the bottom of the heap, requiring O(log N) comparisons and swaps.
            - Average case: O(N log N)
                On average, the node will need to be moved down through a small portion of the heap, so the complexity remains O(log N).


            Total Space Complexity: O(N)  
            input space + auxiliary space = O(N) + O(1) = O(N) 
            
            Auxiliary Space: O(1) 
            No need extra space to store 
        """
        child = 2 * i # The index of the left child node
        n = len(self.array) - 1 
        while child <= n:
            # Check if the right child exists and is larger than the left child
            if child < n  and self.array[child + 1] > self.array[child]:
                child += 1

            # If the current node is smaller than the largest child, swap them
            if self.array[i] < self.array[child]:
                self.array[i], self.array[child] = self.array[child], self.array[i]
                i = child
                child = 2 * i
            else:
                break

def heapsort(array):
    """
    Heap sort is a comparison-based sorting technique.
    It used to sort an array in O(log n)

    Parameters:
        array (array[int]): The array that need to be sorted
       
    Returns:
        -

    Complexity:
        Time Complexity: 
        -Best case: O(N)
            The node is already in the correct position
        - Worst case: O(N log N) 
            every loop (for n times) the delete function is in the worst case which requires O(log n).
        - Average case: O(N log N)
            

        Total Space Complexity: O(N)  
        
        Auxiliary Space: O(1) 
        -   No need extra space to store
    """
    n = len(array)
    heap = MaxHeap(n)

    heap.heapify(array) #Build the heap

    for i in range (heap.max_size, 0, -1): #extract the max element from the heap 
        array[i] = heap.delete()

    return array
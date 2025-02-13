"""
Select minimum is a simple algorithm to retrieve the minimum element in the array,
by using for loop to loop through every element in the array,
and compare it with the previous minimum element.
"""
def select_minimum_function(array):
    min = array[0]
    for index in range(1, len(array)):
        if array[index] < min:
            min = array[index]
    return min
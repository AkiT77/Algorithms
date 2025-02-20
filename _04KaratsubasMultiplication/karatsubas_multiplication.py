"""
Karatsuba's multiplication:
    Base case: If both numbers are less than 10, it directly multiplies them and return.
    Recursive Case: For larger numbers, 
                        the algorithm splits each number into two halves and recursively processes these parts until reaching the base case.
    Combining the results: After computing the recursive results, it combines them into the final product.

main equation: 
x * y = xM * yM * 10**n + xM * yL * 10**n/2 +xL * yM * 10**n/2 + xL * yL
x * y = xM * yM * 10**n + (xM * yL + xL * yM) * 10**n/2 + xL * yL
"""
def karatsubas_multiplication_function(x, y):
    """
    Multiply two numbers using Karatsuba's algorithm with three recursive subproblems.
    
    Parameters:
        x (int): The first number to multiply.
        y (int): The second number to multiply.
    
    Returns:
        int: The product of x and y.

    Complexity:
        Time Complexity: O(n**log2(3)) 
        Since the problem is divided into subproblems of size n/2, and there are three recursive multiplications

        Total Space Complexity: O(log N)  
        input space + auxiliary space = O(1) + O(log N) 
        
        Auxiliary Space: O(log N) 
        Recursive depth
    """
    if 0 <= x < 10 and 0 <= y < 10:
        return x * y
    
    max_len = max(len(str(x)), len(str(y)))
    half_len = max_len // 2
    x_high = x // 10**half_len  
    x_low = x % 10**half_len   
    y_high = y // 10**half_len  
    y_low = y % 10**half_len    

    sum_x = x_high + x_low  # u -> sum_x
    sum_y = y_high + y_low  # v -> sum_y
    a = karatsubas_multiplication_function(x_high, y_high) 
    b = karatsubas_multiplication_function(x_low, y_low)
    c = karatsubas_multiplication_function(sum_x, sum_y)  

    z = c - a - b  
    result = a * 10**(2*half_len) + z * 10**half_len + b
    return result

a = 1234
b = 5678
print(karatsubas_multiplication_function(a, b))
    
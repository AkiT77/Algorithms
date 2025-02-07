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
    
    n = max(len(str(x)), len(str(y)))
    half = n // 2
    xM = x // 10**half
    xL = x % 10**half
    yM = y // 10**half
    yL = y % 10**half

    u = xM + xL
    v = yM + yL
    a = karatsubas_multiplication_function(xM, yM)  
    b = karatsubas_multiplication_function(xL, yL) 
    c = karatsubas_multiplication_function(u, v)  

    z = c - a - b  
    result = a * 10**(2*half) + z * 10**half + b
    return result

a = 1234
b = 5678
print(karatsubas_multiplication_function(a, b))
    
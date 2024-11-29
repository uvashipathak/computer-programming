def calculate_power(base, exp):
    """
    Problem 6: Implement a function to calculate base^exp without using the built-in power function.
    Input: base = 2, exp = 3
    Output: 8
    Explanation: 2^3 = 8.
    """
    result = 1
    for _ in range(exp):
        result *= base
    return result
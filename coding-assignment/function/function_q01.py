def calculate_factorial(n):
    """
    Problem 1: Write a function to calculate the factorial of a number.
    Input: n = 5
    Output: 120
    Explanation: Factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
    """
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)
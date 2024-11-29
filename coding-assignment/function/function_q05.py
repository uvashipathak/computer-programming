def gcd(a, b):
    """
    Problem 5: Write a function to find the GCD of two numbers.
    Input: a = 54, b = 24
    Output: 6
    Explanation: The greatest common divisor of 54 and 24 is 6.
    """
    while b:
        a, b = b, a % b
    return a
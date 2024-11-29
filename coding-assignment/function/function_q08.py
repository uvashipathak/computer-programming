def find_factors(n):
    """
    Problem 8: Write a function to find all factors of a number.
    Input: n = 28
    Output: [1, 2, 4, 7, 14, 28]
    Explanation: These are all divisors of 28.
    """
    return [i for i in range(1, n + 1) if n % i == 0]

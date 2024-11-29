from function_q08 import find_factors
def check_perfect_number(n):
    """
    Problem 9: Write a function to check if a number is a perfect number.
    Input: n = 28
    Output: True
    Explanation: The sum of divisors of 28 (excluding itself) is 1 + 2 + 4 + 7 + 14 = 28.
    """
    return sum(find_factors(n)[:-1]) == n
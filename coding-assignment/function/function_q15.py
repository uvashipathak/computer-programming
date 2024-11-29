from function_q01 import calculate_factorial
from function_q13 import sum_of_digits

def factorial_digit_sum(n):
    """
    Problem 15: Write a function to find the sum of the digits of a factorial.
    Input: n = 5
    Output: 3
    Explanation: 5! = 120, and 1 + 2 + 0 = 3.
    """
    factorial = calculate_factorial(n)
    return sum_of_digits(factorial)
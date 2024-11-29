from function_q01 import calculate_factorial
def check_strong_number(n):
    """
    Problem 20: Write a function to check if a number is a strong number.
    Input: n = 145
    Output: True
    Explanation: 145 = 1! + 4! + 5! = 145.
    """
    return sum(calculate_factorial(int(digit)) for digit in str(n)) == n
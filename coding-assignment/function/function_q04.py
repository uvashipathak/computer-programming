def is_armstrong_number(n):
    """
    Problem 4: Write a function to check if a number is an Armstrong number.
    Input: n = 153
    Output: True
    Explanation: 153 = 1^3 + 5^3 + 3^3.
    """
    num_str = str(n)
    return sum(int(digit)**len(num_str) for digit in num_str) == n
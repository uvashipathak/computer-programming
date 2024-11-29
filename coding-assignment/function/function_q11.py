def is_harshad_number(n):
    """
    Problem 11: Write a function to check if a number is a Harshad number.
    Input: n = 18
    Output: True
    Explanation: 18 is divisible by the sum of its digits (1 + 8 = 9).
    """
    return n % sum(int(digit) for digit in str(n)) == 0

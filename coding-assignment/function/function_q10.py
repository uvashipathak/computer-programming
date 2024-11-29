def calculate_sum_of_squares(n):
    """
    Problem 10: Write a function to calculate the sum of squares of first n natural numbers.
    Input: n = 3
    Output: 14
    Explanation: 1^2 + 2^2 + 3^2 = 14.
    """
    return sum(i**2 for i in range(1, n + 1))